from django.shortcuts import render
import urllib.request
import json
# Create your views here.

def weather(request):
    if request.method == 'POST':
        city = request.POST['enter']
        search_result = city.replace(" ", "%20")
  # source contain JSON data from API
        global longitude,latitude
        source_weather = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+search_result+'&units=imperial&appid=46868eed279cfe0e7919f07a4b87f369').read() 
        # converting JSON data to a dictionary
        weather_load = json.loads(source_weather)
        # data for variable list_of_data
        weather_data = {
            "country_code": str(weather_load['sys']['country']),
            "longitude": str(weather_load['coord']['lon']),
            "latitude": str(weather_load['coord']['lat']),
            "temp": str(weather_load['main']['temp']) + 'F',
            "pressure": str(weather_load['main']['pressure']),
            "humidity": str(weather_load['main']['humidity']),
        }
        longitude = weather_data['longitude']
        latitude = weather_data["latitude"]
        source_pollution = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/air_pollution?lat='+latitude+'&lon='+longitude+'&appid=0be1e7839601e89aa902e6a97e0ccbb5').read()
        pollution_load = json.loads(source_pollution)
        pollution_locator = pollution_load['list']
        f = weather_data['country_code'] 
        g = weather_data['longitude'] 
        h = weather_data['latitude'] 
        for i in pollution_locator:
            a = i["components"]['so2']
            b = i['components']['co']

        pollution_data = {
            "so2" : str(a),
            "co" : str(b),
        }
        l = pollution_data['so2'] 

        final_data = {
            "country_code" : f,
            "longitude" : g,
            "latitude" : h,
            "so2" : l,
            "co" : b
        }
    else:
        weather_data = {}
    return render(request, "Home.html", final_data)
