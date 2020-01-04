#sendEmail.py
import smtplib, logging, ebaySearch, my_info
from email.message import EmailMessage

# email: sends email of the eBay search results
def email():
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

    #open plain text file to compose message
    with open('search_results.txt', 'r') as fp:
        # Create a text/plain message
        msg = EmailMessage()
        msg.set_content(fp.read())

    msg['Subject'] = 'eBay search results'
    msg['From'] = 'sender email'
    msg['To'] = 'recipient email'

    logging.debug('connecting to mail server..')
    # Create smtp object. The arguments are the domain name and port number.
    # The smtp object below represents a connection an SMTP mail server.
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    logging.debug('connected..')
    s.ehlo()
    s.login(my_info.username, my_info.password)
    s.send_message(msg)
    s.quit()
    logging.debug('message successfully sent.')

# call the function if this file is directly called
if __name__ == '__main__':
    email()
