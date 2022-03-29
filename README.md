# NightFall Weather Application :

Project Members:
* Shaam

* I would like to thank Chettinad Vidyashram and my sir Sathiaraj Thomas for giving me a chance to do this project.
  Computer science is my passion and I appreciate the chance that was given to me.
  
## Introduction and About :

This is my 12th Standard CSC project, where the use of python is mandatory. I made this repository to store all my source code.
<h1 align="center">Nightfall Weather Application</h1>
<p align="center">
<img src="https://raw.githubusercontent.com/Shaam-K/NightFall/0a8bf952212875ee1899ead76a55506f09191c9d/weather_project/weather_app/static/icons/logo.svg" alt="logo" width="100" height="100"/> 
</p>

## TERMS : 
* The project is being hosted by me
* <a href="https://www.gnu.org/licenses/gpl-3.0.en.html">Project under GNU General Public License v3.0</a>
 
* Feel free to see the project :  https://nightfall-app.herokuapp.com/
 ( the website is not mobile friendly )
 
## Minor Bug / Annoyance :
There is a small problem regarding the navigation buttons at the top, when you click on for example "Air", look at the url. "#pollution" which is the id of the button, gets added to the url and you will see the pollution part of the page. When you try to search for another place, it will show the new place but in the pollution area again. This can be fixed with javascript, the implementation seemed a bit tricky to me. So will commit a change if I plan to do it. For now, you can solve this by clicking on the arrow on the bottom of the page which will add "#top" to the url and it should be normal.

## Introduction and About :

 This is my 12th Standard CSC project, where the use of python is mandatory. I made this repository to store all the source code.
* Project : Weather App

   The project named **Nightfall** allows you to gather data that is being broadcasted by weather stations worldwide. All you have to do is type the name of the city in the search bar and you will be able to see information about the weather in graphical representation.
                                                                 
## Description of each technology used:

* API :

    * Also called Application Programming Interface where it acts as the intermediate between 2 applications. For 
      example, you can say that API is the waiter at the hotel, you ask him for food which in this case is "data" and the cook which is the "system / database" makes         it for you based on what you asked.

    * API technology especially RESTful (REST is a method like HTTP) based ones are revolutionary as without it 
      developers would have to download extremely large files of data, and most of the data collected would get outdated quickly.

    * Example of an API : http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key} 

    * Most API's require an API KEY which is used for authorisation so that other people cant send commands on 
     your app. NOTE : Dont leave your api keys as it during production, its a bad idea.

    * I used openweather where it had a weather and pollution api

* DJANGO : 

    * Django is a python framework where it allows for fast and scalable web applications. A framework is an ext
      ension to the programming language. It often has more uses or makes some processes easier to implement. in
      my project Django serves as the one that collects the data from the API and projecting the result to the HTML.

    * When you create a project in django, it automatically generates a template for your project, which includes a
      local server to develop in. To create a web application you need to create an app within django. After you can
      write the logic of the app in views.py. In my project I created a function that searches for a name in a html form. Then it gets the name of the city by the html       form. I used the GET method with form that allows me to send my city to views.py where I create a dictionary that sets parameters on what type of data should be      rendered from the API. The final data is then sent back to the html page. And hence displays the data.
      In my project I created a function that searches for a name in a html form. Then it gets the name of the city by the html form. I used the POST method with form        that allows me to send the city to views.py where I create a dictionary that sets parameters on what type of                     data should be rendered from         the API. The final data is then sent back to the html page. And hence displays the data.
      
    * local server link : http://127.0.0.1:8000/

* W3.CSS :

    * Used along with regular CSS, it helpful for centering multiple elements without repeating code

* CHART.JS :

    * Chart.js is a javascript framework that makes displaying graphs in html easier. It takes data from django dic-
      tionary and then renders out the graph in a html canvas. Canvas do not behave well for responsive web design
      but it was the easiest way for me to send the data coming from django to javascript.

## How to download and use my project:

Before you try to download, search how to install django, also make sure to install django in a virtual env

* Django and Virtual ENV setup : https://www.youtube.com/watch?v=VuETrwKYLTM NOTE : Follow the tutorial till
  6:16.
  
  * run the project in the virtual env, to access the virtual env just type `workon` on the cmd
  * also for this demonstration, my virtual env name is "(django)"

* Step 1 : Click on this link https://github.com/Shaam-K/NightFall Now click on the green color button called 
           "code", you should see an option "Download ZIP" click on that and make sure to extract that folder

* Step 2 : open cmd (command line) and go to the directory of the folder.
           ex : **(django) E:\NightFall-main>** where E:\ is the "NightFall-main" is the folder
           
* Step 3 : Now type : **cd NightFall-main**
           you should get the following result : **(django) E:\NightFall-main\NightFall-main>**

* Step 4 : Now type : **cd weather_project**
           you should get the following result : **(django) E:\NightFall-main\NightFall-main\weather_project>**

* Step 5 : Now type : `python manage.py migrate`
           you should see :

           Operations to perform:
            Apply all migrations: admin, auth, contenttypes, historical_data, sessions

           Running migrations:
            Applying contenttypes.0001_initial... OK
            Applying auth.0001_initial... OK
            Applying admin.0001_initial... OK
            Applying admin.0002_logentry_remove_auto_add... OK
            Applying admin.0003_logentry_add_action_flag_choices... OK
            Applying contenttypes.0002_remove_content_type_name... OK
            Applying auth.0002_alter_permission_name_max_length... OK
            Applying auth.0003_alter_user_email_max_length... OK
            Applying auth.0004_alter_user_username_opts... OK
            Applying auth.0005_alter_user_last_login_null... OK
            Applying auth.0006_require_contenttypes_0002... OK
            Applying auth.0007_alter_validators_add_error_messages... OK
            Applying auth.0008_alter_user_username_max_length... OK
            Applying auth.0009_alter_user_last_name_max_length... OK
            Applying historical_data.0001_initial... OK
            Applying sessions.0001_initial... OK

* Step 6 : Now type : `python manage.py runserver`
           you should see : 

            Watching for file changes with StatReloader
            Performing system checks...

            System check identified no issues (0 silenced).
            August 13, 2021 - 19:06:45
            Django version 3.2.5, using settings 'weather_project.settings'
            Starting development server at http://127.0.0.1:8000/
            Quit the server with CTRL-BREAK.
        
* Step 7 : Now click on this link http://127.0.0.1:8000/ and you should see the website

Thanks for downloading!

## Things I removed / Add the Following :

* I removed my api keys, as it was a security concern :

  * Make your own api keys by creating an account on <a href="https://openweathermap.org/">openweather</a> and generate 2 keys
  * Add the api key in views.py, replace {YOUR API KEY} with your api key for both weather and pollution

* I removed my django key :
 
  * To get your django key, make an empty folder and create an empty django project, then head to settings.py and copy the key from SECRET_KEY to the project
  
* I removed my mapbox key and style :
  
  * get your key and style from mapbox and then add them to the project

# Resoures Used :
* django : https://www.djangoproject.com/
* openweather : https://openweathermap.org/api
* chart.js : https://www.chartjs.org/docs/latest/
* Mapbox : https://www.mapbox.com/
* w3schools : https://www.w3schools.com/
* Google Fonts : https://fonts.google.com/
