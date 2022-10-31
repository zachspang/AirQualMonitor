# AirQualMonitor

Uses geopy to get longitude and latitude for a given zipcode, then passes that to the WAQI api to get a json file with lots of information. From this information a chart
is printed out displaying the current air quality for the given zipcode. The user is then prompted if they want the forecasted PM 2.5 particles for the next week.

## Setup
* pip install requests sty geopy
* Run main.py
