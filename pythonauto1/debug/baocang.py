
# import requests
# url = 'http://dev.nexusftx.com:8801/swap_market/simulation/pric'  
# headers = {"X-Auth-Token":"63043865-be3b-41e1-8119-bc1035b1b4da",'Content-Type':'application/json'}
# data =  { 
#     "symbol":"BTC/USDT",
#     "price":"53665"
# } 
# response = requests.post(url, data=data,headers=headers)  
# print(response.text)  




# http://dev.nexusftx.com:8801/swap_market/simulation/price
# symbol:BTC/USDT
# price:38000

# http://dev.nexusftx.com:8801/market/simulation/price


import requests

url = "http://dev.nexusftx.com:8801/swap_market/simulation/price"

payload = {'symbol': 'BTC/USDT',
'price': '53630.3239'}
files=[

]
headers = {
  'x-auth-token': '7f23f4ea-73be-4e24-b24d-e6616c6a5ce2'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
# dev.nexusftx.com:8801

{"data":'null',"code":0,"message":"Success"}