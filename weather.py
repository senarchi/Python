import requests
import json

city=input("Enter the name of the city: ")

url= f"https://api.weatherapi.com/v1/current.json?key=a70ad07c1acf4ad2a0f145520231305&q={city}"

r=requests.get(url)
# print(r.text)

wdic=json.loads(r.text)
print(wdic["current"]["temp_c"])