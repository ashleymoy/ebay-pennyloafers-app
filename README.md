# Ebay Search

This email search is a Python 3 program that searches for Weejuns pennyloafers on eBay and emails the results to me.

## Prerequisites
Non-built in modules used: smtplib, logging, schedule, requests

## Usage

Python 3
This program can be used by either executing the timer_email.py file in Terminal or on AWS Lambda by executing the lambda_handler() in send_email.py

** IMPORTANT! **
Before executing, input API and email info into my_info.py.
Also, update lines 43-44 in send_email.py with your email info.

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
