# ToDoList
This is a TodoList web application built using the Django framework. It allows users to create, manage and organize their daily tasks.


![Alt text](<Screenshot (112).png>)


#
# Getting started
1.Clone the repository
    https://github.com/thibedi-phathela/DjangoDoList.git

2.Create a virtual environment:
    python -m venv env

3.Activate the virtual environment

4.Generate the database migration files:
    python manage.py makemigrations

5.Apply the database migrations:
    python manage.py migrate

6.Run the application
    python manage.py runserver

# Configuration
The application uses a configuration file named .env to manage sensitive data and settings. Make sure to create this file in the project root directory and populate it with the following variables:

    SECRET_KEY=secret-key
    DEBUG=True

Replace secret-key with a secure and unique secret key for your application.