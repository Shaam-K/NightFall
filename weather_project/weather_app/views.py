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
        source_weather = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+search_result+'&units=metric&appid=API_KEY&lang=en').read() 

        # converting JSON data to a dictionary
        weather_load = json.loads(source_weather)
        # data for variable list_of_data

        display_result = search_result.replace("%20", " ")

        weather_data = {
            "display_result": str(display_result),
            "country_code": str(weather_load['sys']['country']),
            "longitude": str(weather_load['coord']['lon']),
            "latitude": str(weather_load['coord']['lat']),
            "temp": int(weather_load['main']['temp']),
            "pressure": str(weather_load['main']['pressure']),
            "humidity": str(weather_load['main']['humidity']),
            "temp_min": str(weather_load['main']['temp_min']),
            "temp_max": str(weather_load['main']['temp_max']),
            "feels_like": str(weather_load['main']['feels_like']),
            "wind_speed": str(weather_load['wind']['speed']),
            "wind_deg": str(weather_load['wind']['deg']),
            "clouds": str(weather_load['clouds']['all']),
            "icon": weather_load['weather'][0]['icon'],
            "description": str(weather_load['weather'][0]['description'])
        }
        display = weather_data['display_result']
        code = weather_data['country_code'] 
        longitude = weather_data['longitude'] 
        latitude = weather_data['latitude'] 
        temp = weather_data['temp']

        pressure = weather_data['pressure']
        humidity = weather_data['humidity']
        temp_min = weather_data['temp_min']
        temp_max = weather_data['temp_max']
        feels_like = weather_data['feels_like']
        wind_speed = weather_data['wind_speed']
        wind_deg = weather_data['wind_deg']
        clouds = weather_data['clouds']
        icon = weather_data['icon']
        description = weather_data['description']

        source_pollution = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/air_pollution?lat='+latitude+'&lon='+longitude+'&appid=API_KEY').read()
        pollution_load = json.loads(source_pollution)
        pollution_locator = pollution_load['list']
        
        for i in pollution_locator:
            carbon_monoxide = i['components']['co']
            nitric_oxide = i['components']['no']
            nitrogen_dioxide = i['components']['no2']
            ozone = i['components']['o3']
            sulfur_dioxide = i['components']['so2']
            pm_two = i['components']['pm2_5']
            pm_ten = i['components']['pm10']
            ammonia = i['components']['nh3']
            air_quality = i['main']['aqi']

        if air_quality == 1 :
            air_text = "Good"

        elif air_quality == 2 :
            air_text = "Fair"
        
        elif air_quality == 3 :
            air_text = "Moderate"
        
        elif air_quality == 4 :
            air_text = "Poor"
        
        else:
            air_text = "Very Poor"

        pollution_data = {
            "co" : carbon_monoxide,
            "no" : nitric_oxide,
            "no2" : nitrogen_dioxide,
            "o3" : ozone,
            "so2" : sulfur_dioxide,
            "pm2_5" : pm_two,
            "pm10" : pm_ten,
            "nh3" : ammonia,
            "aqi" : air_quality,
            "air_text" : air_text
        }

        co = pollution_data['co']
        no = pollution_data['no']
        no2 = pollution_data['no2']
        o3 = pollution_data['o3']
        so2 = pollution_data['so2']
        pm2_5 = pollution_data['pm2_5']
        pm10 = pollution_data['pm10']
        nh3 = pollution_data['nh3']
        aqi = pollution_data['aqi']

        final_data = []
        
        intermediate_data = {
            "display" : display,
            "country_code" : code,
            "longitude" : float(longitude),
            "latitude" : float(latitude),
            "temp" : float(temp),
            "pressure": float(pressure),
            "humidity" : float(humidity),
            "temp_min" : float(temp_min),
            "temp_max" : float(temp_max),
            "feels_like" : float(feels_like),
            "wind_speed" : float(wind_speed),
            "wind_deg" : float(wind_deg),
            "cloud" : float(clouds),
            "co" : float(co),
            "no" : float(no),
            "no2" : float(no2),
            "o3" : float(o3),
            "so2": float(so2),
            "pm2_5" : float(pm2_5),
            "pm10" : float(pm10),
            "nh3": float(nh3),
            "aqi": float(aqi),
            "air_text" : air_text,
            'icon' : icon,
            'description': description
        }

        final_data.append(intermediate_data)
        context = {'final_data' : final_data}
    else:
        context = {}
    return render(request, "Home.html", context)


def handler404(request, exception):
    return render(request, '404.html', status=404)