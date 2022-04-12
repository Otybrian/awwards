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
 In the homepage, a user is able to login or sign up to be able to to view each project and its details ![Screenshot from 2022-04-12 12-15-43](https://user-images.githubusercontent.com/93243367/162942678-fc02bb10-a999-421e-8eed-c9cc12b71be4.png)
tails.

 
 ###### Posting a project
An authenticated user is able to post their projects in this page 
![Screenshot from 2022-04-12 13-42-48](https://user-images.githubusercontent.com/93243367/162943143-f5c03157-b902-4e10-9627-3ef55b80817d.png)



 ###### Login
An existing user enters their details here to login. There is an option for signing up for new users.
![Screenshot from 2022-04-12 13-43-07](https://user-images.githubusercontent.com/93243367/162943182-a19ac9e2-dd1f-49d7-892d-e04836c64344.png)
###### Sign up page

![Screenshot from 2022-04-12 13-43-18](https://user-images.githubusercontent.com/93243367/162943437-1f0001d6-995c-476d-8ad2-8d7beec40ead.png)





 ###### Rating a Project 
  ![Screenshot from 2022-04-12 12-45-42](https://user-images.githubusercontent.com/93243367/162942814-2c08273e-f070-47ac-bfc9-a2c4808091a2.png)

 
 
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
 
