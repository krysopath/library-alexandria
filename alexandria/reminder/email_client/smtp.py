from smtplib import SMTP_SSL as SMTP
from ..templater import email_htm_reminder, compose


def establish_conn(debug=False):
    try:
        conn = SMTP('smtp.gmail.com')
        conn.set_debuglevel(debug)
        conn.login(
            'username',
            "password"
        )
    except Exception as e:
        raise e
    return conn


def send(from_addr, to_addr, msg):
        conn = establish_conn()
        try:
            conn.sendmail(
                from_addr,
                to_addr,
                msg.as_string()
            )
        finally:
            conn.close()



class Admin:
    name = "Georg vom Endt"
    email = "krysopath@gmail.com"


class Testuser:
    name = "Tanja König"
    email = "krysopath@gmail.com"
    admin = Admin


books = ['book1', 'book2', 'book3']

mailcontent = {
    'subject': "library",
    'student': Testuser,
    'books': books
}


send(
    Admin.email,
    Testuser.email,
    compose(mailcontent)
) # sendet ne email
