import smtplib
from email.message import EmailMessage
     

def email_notification(email_subject, email_content):
    """
    two arguments:
    type of email_subject - string
    type of email_content - string
    """
    
    to_email = 'placeholder'
    from_email = 'placeholder'

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
        smtp.login("placeholder", "placeholder")
        
        smtp.send_message(msg)



# testing
print('sending')
email_notification('py test email subject', 'py test email content')
print('sent')
# working emailing function