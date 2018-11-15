import imaplib
from getpass import getpass
import re
import email

list_response_pattern = re.compile(
    r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)'
)


def parse_list_response(line):
    match = list_response_pattern.match(line.decode('utf-8'))
    flags, delimiter, mailbox_name = match.groups()
    mailbox_name = mailbox_name.strip('"')
    return (flags, delimiter, mailbox_name)


def open_imap(credentials, verbose=False):
    """

    :param credentials: {'username': 'john', 'password': 'abc', 'hostname': 'imap.domain.org'}
    :param verbose:
    :return: imap connection
    """
    # Read the config file
    # config = configparser.ConfigParser()
    # config.read([os.path.expanduser('~/.pymotw')])

    # Connect to the server
    # hostname = config.get('server', 'hostname')

    if verbose:
        print('Connecting to', credentials['hostname'])
    connection = imaplib.IMAP4_SSL(credentials['hostname'])

    # Login to our account
    # username = config.get('account', 'username')
    # password = config.get('account', 'password')

    if verbose:
        print('Logging in as', credentials['username'])

    connection.login(
        credentials['username'],
        credentials['password']
    )
    return connection


def parse_emails(response_data):
    if response_data[0] == "OK":
        emails = {}

        for mailmsg in response_data[1]:
            if isinstance(mailmsg, tuple):
                info, msg = mailmsg
                info, msg = info.decode(), msg.decode()
                item = email.message_from_string(msg)
                emails[info.split(' ')[0]] = item

        return emails


def parse_mailid_strings(ids):
    result = []

    for _ in ids:
        w = _.decode()
        result += w.split(' ')
    return result


def build_criteria(crit=None):
    if not crit:
        return "ALL"
    else:
        s = ""
        for c in crit:
            if c == "from":
                add = 'FROM "{}"'.format(crit['from'])
            if c == "subject":
                add = 'SUBJECT "{}"'.format(crit['subject'])

            s += add + " "

        s = s[0:-1]

        return "(%s)" % s


class EmailMixin(object):
    def __init__(self, creds):
        self.creds = creds
        self.connection = None
        self.fetched = None

    def connect_imap(self):
        print(
            "[email_credentials] imap4_ssl://%s:*****@%s" % (
                self.creds['username'], self.creds['hostname']
            )
        )
        self.connection = open_imap(self.creds)
        if self.connection:
            print("[email_connection] %s" % self.connection)

    def list(self):
        return self.connection.list()

    def select(self, box="INBOX"):
        typ, data = self.connection.select(box)
        num_msgs = int(data[0])
        print('[email_mailbox] %s contains %s messsages' % (box, num_msgs))

    def search(self, crit=None):
        typ, msg_ids = self.connection.search(
            None, build_criteria(crit)
        )
        return parse_mailid_strings(msg_ids)

    def fetch(self, _id):
        return parse_emails(
            self.connection.fetch(_id, '(RFC822)')
        )

    def cmd_showmails(self, msg, args):
        self.connect_imap()
        self.select('INBOX')

        if self.connection:
            crit = {}
            for c in args:
                k, v = c.split('=')
                crit[k] = v

            mailids = self.search(crit or None)
            return str(mailids)


if __name__ == '__main__':
    creds = {
        'username': "username",
        'password': "pass",
        'hostname': "imap.gmail.com"
    }

    mailbox = EmailMixin(creds)
    mailbox.connect_imap()
    mailbox.select("INBOX")

    which = ",".join(
        mailbox.search(
            {#'subject': "test",
             'from': "alexandria@email.com"}
        )
    )

    mails = mailbox.fetch(which)
    
    print(mails)

    for k, v in mails.items():
        with open(str(k), 'wb') as mf:
            mf.write(bytes(v))
