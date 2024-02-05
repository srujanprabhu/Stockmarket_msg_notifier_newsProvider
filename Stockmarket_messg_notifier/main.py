import requests
from twilio.rest import Client
STOCK = "TSLA"  #Tesla Company
API_KEY = ""  #Entey your API key
COMPANY_NAME = "Tesla Inc"
parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : API_KEY
}


from datetime import datetime,timedelta
currdate = datetime.now()
currdatee = currdate.date().strftime("%Y-%m-%d")
yester = currdate - timedelta(days=4)
yester2 = currdate - timedelta(days=5)
form_yester = yester.strftime("%Y-%m-%d")
form_yester2 = yester2.strftime("%Y-%m-%d")


parameters2 = {
    "q" : STOCK,
    "from": form_yester2,
    "sortBy" : "popularity",
    "apikey" : "" #Your API key
}
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url="https://www.alphavantage.co/query",params=parameters)
#print(response)
response.raise_for_status()
data = response.json()
yesterday_data = data["Time Series (Daily)"][form_yester]["4. close"]
int_yesterday_Data = float(yesterday_data)
#print(yesterday_data)
daybefore_yes_data = data["Time Series (Daily)"][form_yester2]["1. open"]
#print(daybefore_yes_data)
diff = float(daybefore_yes_data) - float(yesterday_data)
diff_per = 0.01 * float(yesterday_data)
if diff >= diff_per or diff <= diff_per:
    print("Get news")
    response2 = requests.get(url="https://newsapi.org/v2/everything",params=parameters2)
    data2 = response2.json()
    #print(data2)

    parameters2 = {
        "q": STOCK,
        "from": form_yester,
        "sortBy": "popularity",
        "apikey": "" # your API
    }

    account_sid = ""  #These both are available in website
    auth_token = ""
    client = Client(account_sid, auth_token)

    response2 = requests.get(url="https://newsapi.org/v2/everything", params=parameters2)
    data2 = response2.json()
    ar = data2["articles"][0]["title"]
    con = data2["articles"][0]["content"]
    message = client.messages.create(body=f"{ar}\n{con}", from_="+1 814 328 7859", to="=")  #Enter the number
    print(message.sid)





