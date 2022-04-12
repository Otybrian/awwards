# awwards

>[Brian Otieno](https://github.com/Otybrian)  
  
# Description  
This project allows users to post their projects for other users to rate according to design, usability and content 
##  Live Link  

  

## User Story  
  
* A user can view posted projects and their details.  
* A user can post a project to be rated/reviewed. 
* A user can rate/ review other users' projects.  
* Search for projects.  
* View projects overall score.
* A user can view their profile page.  


## Screenshots 
###### Home page
 In the homepage, a user is able to login or sign up to be able to to view each project and its details.

 
 ###### Posting a project
An authenticated user is able to post their projects in this page 

 ###### Login
An existing user enters their details here to login. There is an option for signing up for new users.

 ###### Rating a Project 
  
 
 
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 2.0](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [otbrayo@gmail.com]  
  
  ### Api Endpoints


    
## Setup and Installation  
Get the project in your local computer  
  
##### Cloning the repository:  
 ```bash 
 
```
##### Navigate into the folder and install requirements  
 ```bash 
-pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
-virtualenv virtual
-source virtual/bin/activate 
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations instagram
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`. 
 
