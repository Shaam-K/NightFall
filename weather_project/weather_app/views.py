from django.conf.urls import url
from django.shortcuts import render
import urllib.request
import json
# Create your views here.
def homepage(request):
    if request.method == 'GET':
        city = request.GET['location']
  # source contain JSON data from API
  
        source_weather = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=46868eed279cfe0e7919f07a4b87f369').read() 
        # converting JSON data to a dictionary
        weather_load = json.loads(source_weather)
  
        # data for variable list_of_data
        weather_data = {
            "country_code": str(weather_load['sys']['country']),
            "longitude": str(weather_load['coord']['lon']),
            "latitude": str(weather_load['coord']['lat']),
            "temp": str(weather_load['main']['temp']) + 'k',
            "pressure": str(weather_load['main']['pressure']),
            "humidity": str(weather_load['main']['humidity']),
        }
        print(weather_data)
        longitude = weather_data['longitude']
        latitude = weather_data["latitude"]
        source_pollution = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/air_pollution?lat='+latitude+'&lon='+longitude+'&appid=0be1e7839601e89aa902e6a97e0ccbb5').read()
        pollution_load = json.loads(source_pollution)

        print(pollution_load)
    else:
        weather_data = {}

    return render(request, "Home.html", weather_data)