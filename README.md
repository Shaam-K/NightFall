# NightFall :

## Introduction and About :


    This is my 12th Standard CSC project, where the use of python is mandatory. I made this repository to store all my source code.

* Project : Weather App

    My project named **Nightfall** allows you to gather data that is being broadcasted by weather stations. All you have to do is type the name of the city in the search bar and you will be able to see information about the weather in graphical representation.

*  Languages / Frameworks Used:

    * HTML 
    
    * CSS
        * W3.CSS
        
    * JAVASCRIPT
        * CHART.JS

    * PYTHON
        * DJANGO

## Description of each technology used:

* API : 
    ![Image of API](https://cdn.artandlogic.com/wp-content/uploads/django.jpeg)

    * Also called Application Programming Interface where it acts as the intermediate between 2 applications. For 
      example, you can say that API is the waiter at the hotel, you ask him for food which in this case is "data" and the cook which is the "system / database" makes it for you based on what you asked.

    * API technology especially RESTful (REST is a method like HTTP) based ones are revolutionary as without it 
      developers would have to download extremely large files of data, and most of the data collected would get outdated quickly.

    * Example of an API :(http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}) 

    * Most API's require an API KEY which is used for authorisation so that other people cant send commands on 
     your app. NOTE : Dont leave your api keys as it during production, its an bad idea.

    * I used openweather where it had a weather and pollution api

* DJANGO : 
    * Django is a python framework where it allows for fast and scalable web applications. A framework is an ext
      ension to the programming language. It often has more uses or makes some processes easier to implement. in
      my project Django serves as the one that collects the data from the API and projecting the result to the HTML.

    * When you create a project in django, it automatically generates a template for your project, which includes a
      local server to develop in. To create a web application you need to create an app within django. After you can
      write the logic of the app in views.py. In my project I created a function that searches for a name in a html form. Then it gets the name of the city by the html form. I used the GET method with form that allows me to send my city to views.py where I create a dictionary that sets parameters on what type of data should be rendered from the API. The final data is then sent back to the html page. And hence displays the data.

    * local server link : (http://127.0.0.1:8000/)

* W3.CSS :
    * Used along with regular CSS, it helpful for centering multiple elements without repeating code

* CHART.JS : 
    * Chart.js is a javascript framework that makes displaying graphs in html easier. It takes data from django dic-
      tionary and then renders out the graph in a html canvas. Canvas do not behave well for responsive web design
      but it was the easiest way for me to send the data coming from django to javascript.

---
Project Members:
* Shaam
    * Class : 12 D
    * Roll No : 43
---
