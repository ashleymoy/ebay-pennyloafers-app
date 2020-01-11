# Ebay Search

This email search is a Python 3 program that searches for Weejuns pennyloafers on eBay and emails the results to me.

## AWS Branch
The AWS branch was formatted for use with AWS Lambda and SES (Simple Email Service). The daily timer function is triggered by a CloudWatch Events rule. The email is sent with boto3

## Prerequisites
Non-built in modules used: smtplib, logging, schedule, requests, boto3

## Usage

Python 3
This program can be used by either executing the timer_email.py file in Terminal or on AWS Lambda by executing the lambda_handler() in send_email.py

** IMPORTANT! **
Before executing, input API info into lines 28-30 of send_email.py.
Also, input email information into lines 35 and 49.

## Author

* **Ashley Moy** - [Ashley Moy](https://github.com/ashleymoy)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

I had the idea to make this program after wasting time searching on Ebay for the products I wanted.

This was my first coding project and I learned a lot, including the following:

- Working with RESTful APIs, reading documentation, parsing API responses, etc.
- Using AWS services: Lambda, Cloudwatch Events, SES, IAM
- Making multiple python files work with each other
- How to send outgoing email using smtplib module
- Working with json module
- How to log/debug with logging module
- Creating a README and LICENSE
- Setting a function to execute on an interval
- Using Git and Github
- Crons
