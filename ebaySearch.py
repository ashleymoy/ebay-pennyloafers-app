#ebaySearch.py
import my_info
import requests, json, logging

def ebaySearchAPI():
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    url = ('https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SECURITY-APPNAME=' + my_info.api_token + '&RESPONSE-DATA-FORMAT=JSON&aspectFilter=15&itemFilter(0).name=MaxPrice&itemFilter(0).value=100&itemFilter(0).paramName=Currency&itemFilter(0).paramValue=USD&itemFilter(1).name=Condition&itemFilter(1).value(0)=New&itemFilter(1).value(1)=1000&itemFilter(1).value(2)=1500&itemFilter(1).value(3)=2000&itemFilter(1).value(4)=4000&entriesPerPage=20&keywords=weejuns%20black%207')
    # &searchResult.item.listingInfo.2019-12-09T00:00:00.000Z
    logging.debug('searching ebay..')
    # get data from api and put it into json format
    res = requests.get(url).json()

    # checkpoint to test status output
    if requests.get(url).status_code != 200:
        print(requests.get(url).status_code)
    logging.debug('getting results..')

    # parse json data into a dict
    results = {}
    for item in (res['findItemsByKeywordsResponse'][0]['searchResult'][0]['item']):
        title = (item['title'][0])
        viewItemURL = (item['viewItemURL'][0])
        if title not in results.keys():
            results[title] = viewItemURL

    # write results to text file
    with open('SearchResults.txt', 'w') as fp:
        fp.writelines((json.dumps(results)))

    # print results if this file is directly called
    if __name__ == '__main__':
        print(results)
    else:
        return results

# call the function if this file is directly called
if __name__ == '__main__':
    ebaySearchAPI()
