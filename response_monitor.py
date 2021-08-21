import smtplib
from email.message import EmailMessage
import requests
from config import password_1, email_1
# config file with a login information for a gmail account 
import time
from datetime import datetime


def status_code(website_address):
    r = requests.get(website_address, timeout=8)
    return r.ok


def email_notification(email_subject='Server is down!', email_content='...'):
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


def main():
    while True:
        try:
            address = input('website address: ')
            code_return = status_code(address)
            print(code_return)
            break
        except Exception as e:
            print('Wrong input, try again.')
            print('Don\'t forget about https://...')
            continue
    
    while True:
        if code_return:
            print('Server is up, ' + str(datetime.now()) + ', ' + address)
            time.sleep(20 * 60)
            # checks a status code every 20 minutes
            continue
        else:
            email_notification()
            print('Server is down, notification email has been sent')
            break


if __name__ == '__main__':
    main()
