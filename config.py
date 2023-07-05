

"""Команда для консоли:

    python -m smtpd -n -c DebuggingServer localhost:25

     - запускает отладочный сервер SMTP, который нам предоставляет Python
    
    Команды для консоли после команды python:
 #           >>> from flask_mail import Message
 #           >>> from app import app, mail
 #           >>> from config import ADMINS
 #           >>> msg = Message('test subject', sender = ADMINS[0], recipients = ADMINS)
 #           >>> msg.body = 'FGHJKL:LKNBVCVHJKLOIUFDSFYIOPIGFDFLKHFDCFGHKL:+++++++++++++++++'
 #           >>> msg.html = '<b>HTML</b> body'
 #           >>> app.app_context().push()
 #           >>> mail.send(msg)    """


# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT =587 #465 #
MAIL_USE_TLS = True #False
MAIL_USE_SSL = False #True
MAIL_USERNAME = 'TatyArt.Knit@gmail.com'
MAIL_PASSWORD = '494348622Klava'

# administrator list
ADMINS = ['levmoskvitin@gmail.com']