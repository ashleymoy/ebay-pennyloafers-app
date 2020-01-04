# sends email on a timed interval.
from send_email import email
import schedule, time, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

schedule.every().day.at("10:00").do(email)

logging.debug('job scheduled..')

while True:
    schedule.run_pending()
    time.sleep(1) # wait one second
