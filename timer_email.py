# sends email on a timed interval.
from send_email import sendEmail
import schedule, time, logging, json

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

def email_timer():
    schedule.every().day.at("10:00").do(sendEmail)
    while True:
      schedule.run_pending()
      logging.debug('job scheduled..')
      time.sleep(1) # wait one second

# lambda handler function
def lambda_handler(event, context):
    email_timer()
    return {
        'statusCode': 200,
        'body': json.dumps('Woohoooo!')
    }

# call the function if this file is directly called
#if __name__ == '__main__':
#    email_timer()
