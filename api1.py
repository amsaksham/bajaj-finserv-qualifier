import requests
import json

url = "https://customer-analytics-34146.my.salesforce-sites.com/services/apexrest/createAccount"

payload = json.dumps({
  "name": "Saksham",
  "email": "saksham6001.be21@chitkara.edu.in",
  "rollNumber": 2110996001,
  "phone": 9466521789
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'BrowserId=EqvFWOUIEe6OF9Vmbon52Q; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
