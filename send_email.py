import logging, requests, json, my_info, boto3

# lambda handler function
def lambda_handler(event, context):
    #ebay search
    url = ('https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SECURITY-APPNAME=' + my_info.api_token + '&RESPONSE-DATA-FORMAT=JSON&aspectFilter=15&itemFilter(0).name=MaxPrice&itemFilter(0).value=100&itemFilter(0).paramName=Currency&itemFilter(0).paramValue=USD&itemFilter(1).name=Condition&itemFilter(1).value(0)=New&itemFilter(1).value(1)=1000&itemFilter(1).value(2)=1500&itemFilter(1).value(3)=2000&itemFilter(1).value(4)=4000&entriesPerPage=20&keywords=weejuns%20black%207')

    # get data from api and put it into json format
    res = requests.get(url).json()

    # parse results into dict
    results = {}
    for item in (res['findItemsByKeywordsResponse'][0]['searchResult'][0]['item']):
        title = (item['title'][0])
        viewItemURL = (item['viewItemURL'][0])
        if title not in results.keys():
            results[title] = viewItemURL

    # create email body
    emailBody = ""
    for i in results:
        emailBody += json.dumps(i) + "\n"
        emailBody += str(results[i]) + "\n"

    # send email with boto3
    client = boto3.client(
        'ses',
     region_name='insert-region-here',
     aws_access_key_id='aws_access_key_id',
     aws_secret_access_key='aws_secret_access_key'
)

    response = client.send_email(
    Destination={
        'ToAddresses': ['recipient'],
    },
    Message={
        'Body': {
            'Text': {
                'Charset': 'UTF-8',
                'Data': emailBody,
            },
        },
        'Subject': {
            'Charset': 'UTF-8',
            'Data': 'eBay search results',
        },
    },
    Source='sender',
)

    return {
        'statusCode': 200,
        'body': json.dumps('Email sent.')}
