Project work for Cyber Security Base course

Project works at least with Python 3.8 and Django 4.0 versions. 
Download files to your computer, go to directory mysite/ and run commands:

'python manage.py migrate'

'python manage.py runserver'

Then open your browser and go to the address: 

http://127.0.0.1:8000/polls/

You can register new users and log in as existing user. When successfully logged in, you are redirected to the page where a message Successfully logged in is displayed. If registering or logging in fails, home page is reloaded without any error message.

Implemented security vulnerabilities (from OWASP 2021 top ten):

CSRF

Injection

Identification and authentication failures

Security misconfiguration

Broken access control
