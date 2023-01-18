# Humanity

Check out a [video](https://youtu.be/LoPxcdcfaLc) I made going over the main features of the web app!

[![Humanity - A Web App](https://img.youtube.com/vi/LoPxcdcfaLc/0.jpg)](https://youtu.be/LoPxcdcfaLc)

<hr>

Hello, my name is Santiago Giner and I am a student at Harvard College concentrating in physics and computer science. This is my final project for the course CS50. It is a web application designed with the Django framework and is intended for users of every age. The main objective of the project is to provide people with the chance to record their life's journey. In order to do this, the website has several different features that allow for things like keeping track of goals, projects, and books the user is reading, journaling, or even writing messages to your future self. It is now, in 2020, more important than ever to find times to focus on what really matters to you, to do the things you like, and to accomplish the goals you have. I hope this time capsule can aid you in doing that.

## Heroku
Humanity has also been deployed to the Heroku cloud platform, where it can be accessed anytime and anywhere as long as the user has an internet connection. The link to the website is: https://humanityproject.herokuapp.com/

## Features
As explained above, the main feature of Humanity is providing a way for the user to record their life, which is why the main application of the project is called "Time Capsule." Firstly, the user has to register for an account and can then log in and log out as desired. Then, the time capsule presents 5 different sections, each with their own purpose: Journal, Goals, Projects, Mini Capsules, and Library.

### Account
In order to use the site, the user must first create an account by providing a username, first name, last name, email, password, and password confirmation. These fields must all meet different criteria explained in the registration form, namely, the passwords provided must match, they cannot be too similar to the user's first name, last name, or username, the email provided must be a valid one (i.e. contain an @ symbol and a .com, .net, or any other similar suffix), along with other password requirements. It should be noted that the application will not actually check if the email provided is an existing one, it will just check if it has the right structure. Once the user has registered, they will be automatically logged in and "rememebered" by the site, i.e. they will not have to log in again until they click the Log out. Finally, the user can also delete their account by clicking the "Delete account" link in the top navigation bar.

### Default Route of the Time Capsule
The default route of the time capsule application, i.e. "/" renders a template that very briefly details the purpose of the time capsule and also contains a video from YouTube that was originally recorded by Carl Sagan. The video is meant as something to be viewed at the user's leisure and is not part of the application per se, i.e. it is apart from the different features of the app, detailed below.

### Journal
The user can have a journal, wherein by submitting a form that contains the journal entry, said entry gets added to the user-specific journal. Entries are then displayed as links that when clicked will show a page that contains the entry content and allows users to either update the entry or delete it entirely.

### Goals
The user can set daily, weekly, monthly, and long-term goals. The user can switch between the different goals by clicking on the appropriate button at the top of the page. They can then complete these goals by clicking the "Complete goal" button. Completed goals are not deleted, rather, they are marked as completed and thus appear in the "Completed Goals" section. Once completed, a goal can be deleted if the user so chooses.

### Projects
The user can add any projects on which they are working, including the project title, goal time to finish the project, project status, description of the project, and any other relevant information they desire. In the project status, the choices allowed are "completed," "in progress," and "stopped." Once a project has been added, the user can then update any or all of the project's information. They can also add project logs, whereby they record the progress they have been making on their project. These logs can also be subsequently deleted (but not updated). Finally, the user can delete the project entirely, if they so desire.

### Mini Capsules
With this feature, the user can write a message to their future self. They submit a form specifying a message content and a date in which they want to read that message. Then, the message will be displayed only if the current date is on or after the date they specified. Once read, the mini capsules can be deleted.

### Library
In this section of the page are displayed all the books the user has added to their library. In order to add a book, the user must search for one in the "Add Book" section. Their query will then be sent to the Google Books API, and the results of the search will be displayed on the page, including the book's title, author(s), and cover photo. Once the user has selected the book they desire, it will be added to their library and displayed in the "Library" section. Once here, the user can delete the book or write book notes. The "View book" section will display the book's title, author(s), cover photo, as well as the description of the book (as found in the Google Books API). The notes are submitted via a form and can subsequently be updated and/or deleted.
