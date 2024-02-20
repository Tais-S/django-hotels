# Hotels Admin

## Description
This is a sample project to showcase basic Django skills.

## Usage
1. Have Docker and Docker Compose installed on your system to run the project locally using Docker Compose.
2. Clone the repository:
   ~~~ 
   git clone https://https://github.com/Tais-S/django-hotels.git
   ~~~ 
3. Navigate to the project directory.
4. Build and start the Docker container: 
    ~~~ 
    docker-compose up --build 
    ~~~
5. Access the application in your web browser at http://localhost:8000.
6. To navigate to the Register and Login pages, refer to http://localhost:8000/register/ and http://localhost:8000/login/ respectively.

## Accessing Django Admin
To access the Django admin interface, run the following command to create a superuser and enter your desired username, email, and password when prompted:
~~~ 
python manage.py createsuperuser
~~~ 
