# General Overview
Humanity is a web application designed with Django. More precisely, the Django project is titled Humanity and its main (and only) application is titled Capsule (short for time capsule). The purpose of most all the files in the project can be found in the Django Documentation, as they are automatically created when starting a Django project.

# Capsule
The capsule folder is where the main part of the project lies. As mentioned above, it is the main application of the project and handles all the features detailed in the documentation. The capsule folder itself contains various folders and files, including: migrations, static, templates, and several Python files. 

## Migrations
Migrations refer to the interactions with the project's database. Django allows for easy interaction with the database through Python instead of having to explicitly write SQL queries. In models.py is where all the models (i.e. tables in the database) are declared. Then, actions involving storing of new data, updating existing data, deleting data, etc., are all done through the views.py file.

## Templates
Here you can find the HTML of the many different views of the application. They all inherit from the same "layout.html" file, which contains the relevant link for scripts, stylesheets, and the overall base template of all the views. Bootstrap components are used in all the templates, including, but not limited to, navigation bars, buttons, alerts, cards, and modals. Relevant information about these can be found in the Bootstrap documentation. Moreover, when displaying forms, I have used the Django Crispy Forms feature which renders the form in a better-styled way. The fields of the forms themselves are declared in the forms.py file.

## Static
In this folder is where the CSS file of the application is stored, as well as the logo of the site, and the JavaScript files. CSS was not amply used and was simply employed to align some items to the center of the page, change their font color, and/or specify some margins. In "script.js" lies the script that allows the user to toggle a form to either add or update elements like goals, or journal entries. The other JavaScript file, namely, "library.js" performs the searching of books and displaying the results to the user through the use of the Google Books API. The script first finds the input from the user (by getting the value of the text input) and performs a query on the API, with the user's input, as well as a language restriction of English (to only display books in this language), and my particular API Key, which was obtained through the Google Developers site. The script then displays the results, including the book's title, author(s), and/or cover photo. For each of these fields, I included a "hidden input," i.e. an input not displayed to the user such that when the user clicks on the accompanying "Select" button to each book, a form gets submitted via POST which is meant to add the book to the user's library. I decided to include these as hidden inputs and not as inputs that could be modified by the user so as to preserve the integrity of the data from Google Books. Another field stored as input is the book description, which is not displayed to the user but is stored in the database so as to be displayed when the user visits the "Book notes" section of each book.

## Views.py
TODO

## Other relevant Python Files
As mentioned above, the forms.py file create the different forms used in the application as Python classes which can then be called in the "views.py", which is the main controller of the website. In "models.py" is where the database tables are declared, also as Python classes which can be called in "views.py." In "apps.py," the application is given the name of "capsule;" in "urls.py" os where all the url paths of the website are established,including paths for each different feature: logging in/out, deleting account, registering, journal, goals, projects, mini capsules, and the library.

# Humanity
In this folder are located crucial files of the project that are the behind the integration of Django. These are files created automatically by Django and which contain important settings and configurations so as to allow the use of the framework and features like Django Crispy Forms. All the relevant information about these files can be found in the Django Documentation. In this case, the changes made were to the "settings.py" file were I included lines to enable the use of Django Crispy Forms as well as to integrate Heroku into the site and declare it as an allowed host.

# Heroku
In order to integrate Heroku, I first had to include it in the "settings.py" file as by calling <django_heroku.settings(locals())> which will set up the application so as to be hosted by Heroku, and which requires the django-heroku library that can be installed through <pip>.
