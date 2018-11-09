
####Instaclone247


## Instaclone247 is a web app clone of the popular instagram mobile app.
###Created on: october, 25TH,  2018

###Author
By Gabriel Nwachukwu

#### GITHUB Account:**https://github.com/gabrielcoder247**

## Description
Users can post pictures and other user like them, follow them
#features
likes
follow
expand to view details
post pictures




###User Stories
As a user I would like:

to Sign in with the application to start using.
to Set up a profile about me and a general location and my neighborhood name
to find a list of different businesses in my neighborhood.
to create Posts that will be visible to everyone in my neighborhood.
to change My neighborhood when I decide to move out
to view details of a single neighborhood.

## Specifications
Get the specs [here](https://github.com/gabrielcoder247/pitch-v2.0/blob/master/SPECS.md)

## Set-up and Installation

### Prerequiites
    - Python 3.6
    - Ubuntu software

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/gabrielcoder247/pitch-v2.0 && cd PitchIt on your machine terminal`

Install [Postgres](https://www.postgresql.org/download/)

### Create a Virtual Environment
Run the following commands in the same terminal:
`sudo apt-get install python3.6-venv`
`python3.6 -m venv virtual`
`source virtual/bin/activate, to activate the virtual environment`

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements`


### Run Database Migrations
```
python manage.py db makemigrations <app name>
python manage.py db migrate 

```

### Running the app in development
In the same terminal type:
`python3 manage.py runserver`

Open the browser on `http://localhost:8000/`


#### Dependancy Installments

pip3 install python3.6
pip3 install django==1.11 django-heroku gunicorn pillow whitenoise python-decouple psycopg2-binary django-bootstrap3

## Known bugs
It does not have bugs.But if any problems should occur,you can contact me on the address below

N/B The finished product yet read ...more features and functionalities are still being worked on.


## Technologies used
    - Python 3.6
    -Django
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details
Contact me on gabrielcoder@gmail.com for any comments, reviews or advice.


### MIT License

Copyright (c) 2018 Dev Gabriel Nwachukwu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.