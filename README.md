# school_mgmt

How to run 

Requirements 

Python 3.8.10   // https://www.python.org/ 

virtualenv  // https://virtualenv.pypa.io/en/latest/installation.html


step 1

create virtualenv and activate it

step 2

clone this repo

step 3

cd school_mgmt

step 4

install required dependencies  // pip install -r requirements.txt

step 5

run server : python manage.py runserver (check it works or not) => if works follow step 6

step 6

python manage.py makemigrations

step 7

python manage.py migrate

step 8

python manage.py createsuperuser (fill all fields with validate data, username must be unique  )


step 9 

localhost:8000

localhost:8000/admin   // school admin side
