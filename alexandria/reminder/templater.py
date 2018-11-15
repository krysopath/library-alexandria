from jinja2 import Environment, FileSystemLoader
from email.mime.text import MIMEText
from . import path

template_path = f'{path}/templates'
print('path to templates', template_path)
env = Environment(
    loader=FileSystemLoader(template_path),
    autoescape='html'
)
email_htm_reminder = env.get_template('reminder.html')


def compose(content):
    s = email_htm_reminder.render(
        student=content['student'],
        books=content['books']
    )
    msg = MIMEText(s, 'html')
    msg['Subject'] = content['subject']
    msg['To'] = content['student'].email
    return msg
