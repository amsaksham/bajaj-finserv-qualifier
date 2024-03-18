import requests
import json

url = "https://customer-analytics-34146.my.salesforce-sites.com/services/apexrest/buyStocks"

payload = json.dumps({
  "company": "BAJAJFINSV",
  "currentPrice": 1577,
  "accountNumber": "BFHL0018662",
  "githubRepoLink": "https://github.com/amsaksham/bajaj-finserv-qualifier"
})
headers = {
  'bfhl-auth': '2110996001',
  'Content-Type': 'application/json',
  'Cookie': 'BrowserId=EqvFWOUIEe6OF9Vmbon52Q; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
