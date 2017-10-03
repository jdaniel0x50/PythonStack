import requests

city_search = "Chicago"
data = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city_search + '&units=imperial&APPID=30e88e4d6348c1b24222c23008a330ea')
json_object = data.json()

print json_object

for keys in json_object:
    print keys
    
city_temp = json_object['main']['temp']

print str(city_temp) + " degrees Farenheit"