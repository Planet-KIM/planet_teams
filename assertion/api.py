import requests, xmltodict, json
import pandas as pd

key = "D4JSnUdp72NPQWZwLqKXR4r2Gx19BtVn6IQIolkhQ1OZsk5qUQ8zOGpYPSdeSk3jmdopnmCY1c45IP8s%2B7DjYg%3D%3D"
url =  "http://apis.data.go.kr/1520635/OceanSatelliteImageInfoService/getOceanSatelliteImageDetail?seq=376463&ServiceKey={}".format(key)

content = requests.get(url).content
dict = xmltodict.parse(content)

jsonString = json.dumps(dict['response']['body'], ensure_ascii= False)

jsonObj = json.loads(jsonString)

for item in jsonObj['items']['item'].items():
    print(item)

file = open("./nonPayment.json", "w+")
file.write(json.dumps(jsonObj['items']['item']))



