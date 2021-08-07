import smtplib
from email.message import EmailMessage
import requests
from config import password_1, email_1
     

def status_code(url):
    r = requests.get(url, timeout=8)
    return r.ok


def email_notification(email_subject, email_content):
    """
    two arguments:
    type(email_subject)- string
    type(email_content)- string
    """
    

    to_email = email_1
    from_email = email_1

    msg = EmailMessage()
    msg['Subject'] = email_subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(email_content)
        
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        # ecnryption
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        
        # use environment variables or configuration file to store your e-mail and password
        smtp.login(email_1, password_1)
        
        smtp.send_message(msg)



# testing
print('sending')
email_notification('py test 2 email subject', 'py test email content ddsds')
print('sent')
# working emailing function