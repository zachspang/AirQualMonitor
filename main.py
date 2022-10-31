#https://geopy.readthedocs.io/en/stable/#nominatim
#https://docs.python-requests.org/en/master/
#https://sty.mewo.dev/index.html




token = ""

zipcode = input("Enter you zipcode: ")

# Finds long and lat from zipcode

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="AirQualityTracker")

location = geolocator.geocode({'postalcode': zipcode})

Latitude = location.latitude
Longitude = location.longitude

#gets data from api

import requests
#print(f"https://api.waqi.info/feed/geo:{Latitude};{Longitude}/?token={token}\n")
r = requests.get(f"https://api.waqi.info/feed/geo:{Latitude};{Longitude}/?token={token}")

data = (r.json())
currentaqi = data['data']['aqi']
print(f"The current Air Quality Index is: {currentaqi}")
print('\n', end = "")

#will set a variable to an arrow to mark on the chart what the saftey level is
AQIg = ""
AQIm = ""
AQIus = ""
AQIu = ""
AQIvu = ""
AQIh = ""

if currentaqi < 51:
  AQIg = " <--- Current AQI level "
elif currentaqi < 101:
  AQIm = " <--- Current AQI level "
elif currentaqi < 151:
  AQIus = " <--- Current AQI level "
elif currentaqi < 201:
  AQIu = " <--- Current AQI level "
elif currentaqi < 301:
  AQIvu = " <--- Current AQI level "
else:
  AQIh = " <--- Current AQI level "


#adds colored backgrounds to be used in a chart

from sty import bg, ef, fg, rs

print(bg(40) + "                Good                " + bg.rs + AQIg)
print(bg(3) + "              Moderate              " + bg.rs + AQIm)
print(bg(214) + "   Unhealthy for Sensitive Groups   " + bg.rs + AQIus)
print(bg(9) + "              Unhealthy             " + bg.rs + AQIu)
print(bg(127) + "           Very Unhealthy           " + bg.rs + AQIvu)
print(bg(52) + "             Hazardous              " + bg.rs + AQIh + "\n")



#gets current date and time and find what index that is on the forecast

currenttime = data['data']['time']['s']
day = currenttime[0:10]
# print(day)

for item in data['data']['forecast']['daily']['pm25']:
  if item['day'] == day:
    forecastindex = data['data']['forecast']['daily']['pm25'].index(item)

#print all available forecasts up to 7 days in the future

wantforecast = input("If you want the forecasted PM2.5 levels please enter Y. Otherwise enter N: ")

if wantforecast == "Y":
  
  print('\n', end = "")
  
  for i in range(6):
    if forecastindex + 1 < len(data['data']['forecast']['daily']['pm25']):
      forecastindex +=1
      
      print (data['data']['forecast']['daily']['pm25'][forecastindex]['day'])
     
      print ("Forecasted PM2.5 level: " + str(data['data']['forecast']['daily']['pm25'][forecastindex]['avg']))
     

      print('\n', end = "")

