# User Management in Django

This tutorial will demonstrate how to manage users in Django. It was made for educational purposes as well as for personal use to prepare the final project of `ft_transcendence` from the `42` main curriculum.  
In this tutorial I cover the basic environment setup in Django as well as the following topics:  
- User login and registration
- User authentication with email and password
- User authentication with Google (OAuth2.0) with `django-allauth`
- User profile page
- Setting up PostgreSQL database instead of the default SQLite3


## To setup the environment for the project:

### ON LINUX:

1. Install `pipenv`.

```bash
pip install pipenv
```

2. Install `django`.

In the project directory (this repo), run:
```bash
pipenv install django
```

3. Activate the virtual environment.

```bash
pipenv shell
```
Alternatively, to have the virtual environment activated automatically with VSCode, do the following:

in command palette (`Ctrl+Shift+P`), search for `Python: Select Interpreter`, and select the virtual environment path created by `pipenv`.  

To check the path of the virtual environment, run `pipenv --venv`.  

**Note**: If the virtual environment is not activated during the next launch select the environment path in VSCode command pallet once more and relaunch the text editor.  


### ON MACOS (M1):

Assuming `Homebrew`, `Python3`, `pip3` are already installed.

1. Install `pipenv` with `pipx`.

```bash
brew install pipx

pipx ensurepath

pipx install pipenv
```

2. Install `django`.

In the project directory (this repo), run:
```bash
pipenv install django
```

3. Activate the virtual environment.

```bash
pipenv shell
```

## Setting Up POSTGRESQL:

### Setting up PostgreSQL database

1. 
....

## Setting Up `OAuth2.0` with `django-allauth` for remote authentication:

### Installing and setting up allauth

1. **Install `django-allauth`.**

In the project directory (this repo), run:
```bash
pipenv install django-allauth
```
or 
```bash
pip install django-allauth
```

2. **Adding the required settings in `settings.py`.**

- Add `AUTHENTICATION_BACKENDS` to the end of `settings.py`.

```python
...
AUTHENTICATION_BACKENDS = [
	'django.contrib.auth.backends.ModelBackend',
]
```

- Add the following `allauth` apps to the `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
	...
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	...
]
```

- Add the following to the `MIDDLEWARE`:

```python
MIDDLEWARE = [
	...
	'allauth.account.middleware.AccountMiddleware',
	'allauth.account.auth_backends.AuthenticationBackend',
]
```

3. **Add the following to the `urls.py`:**

```python
urlpatterns = [
	...
	path('accounts/', include('allauth.urls')),
]
```

- Add the following lines to the end of the `settings.py`:

```python
SOCIALACCOUNT_PROVIDERS = {} # to add social providers later if needed (not necessary, can be specified in the database)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # to print emails in the console for testing purposes

ACCOUNT_AUTHENTICATION_METHOD = 'email' # to use email as the authentication method
ACCOUNT_EMAIL_REQUIRED = True # this will make the email as obligatory field
```

*At this point we can run the server and register a new user with email and password.  
Once this done we can see automatic message in the console that the email was sent to verify the account.  
We can copy the verification link and paste it in the browser to complete the verification of the account.  
After that we can see in the admin panel that given user is active and that the email is verified.*  


4. **Adding an examle of the profile page:**

- In the `users/views.py` adding the following:

```python
...
def profile(request):
	return render(request, 'users/profile.html', name='profile')
```

- In the `users/templates/users` creating the `profile.html` file:

```html
{% extends "layout.html" %}

{% block title %}
	<title>Profile Page</title>
{% endblock title %}

{% block content %}
	<h1>This is your profile page. You are logged in as [{{ request.user.username }}]</h1>

	<a href="{% url 'users:logout' %}">Logout</a>
{% endblock content %}

```

- In the `users/urls.py` adding the following:

```python
...
urlpatterns = [
	...
	path('profile/', views.profile, name='profile'),
]
```

Once the server is running we can navigate to the `localhost:8000/users/profile/` and see basic profile page with the username of the logged in user and a logout link.  


**NOTE**: *These are the available pages withing the `allauth` package that can be utilised:*

```text
01. accounts/ login/ [name='account_login']
02. accounts/ logout/ [name='account_logout']
03. accounts/ inactive/ [name='account_inactive']
04. accounts/ signup/ [name='account_signup']
05. accounts/ reauthenticate/ [name='account_reauthenticate']
06. accounts/ email/ [name='account_email']
07. accounts/ confirm-email/ [name='account_email_verification_sent']
08. accounts/ ^confirm-email/(?P<key>[-:\w]+)/$ [name='account_confirm_email']
09. accounts/ password/change/ [name='account_change_password']
10. accounts/ password/set/ [name='account_set_password']
11. accounts/ password/reset/ [name='account_reset_password']
12. accounts/ password/reset/done/ [name='account_reset_password_done']
13. accounts/ ^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$ [name='account_reset_password_from_key']
14. accounts/ password/reset/key/done/ [name='account_reset_password_from_key_done']
15. accounts/ 3rdparty/
16. accounts/ social/login/cancelled/
17. accounts/ social/login/error/
18. accounts/ social/signup/
19. accounts/ social/connections/
```


## Adding authentication via Google:

1. **Installing necessary dependencies:**

```bash
pipenv install requests

pipenv install PyJWT

pipenv install cryptography

```

2. **Add the following to the `settings.py` `INSTALLED_APPS`:**

```python
...
INSTALLED_APPS = [
	...
	'allauth.socialaccount.providers.google',
	...
]
```

3. **Adding Social Application in django admin panel:**

- Go to `localhost:8000/admin/` and login with the superuser credentials.  

Then go to --> `Social applications` --> `Add social application`  

*Fill in the following fields:*  
Provider: `Google`  
Name: `Google`  
Client id: `'your_client_id'`  see below how to get it   
Secret key: `'your_secret_key'` see below how to get it  

- Getting `client_id` and `secret_key` from Google Cloud Console:

To get the `client_id` and `secret_key` go to your -> [Google Cloud Console](https://console.cloud.google.com/).  

Navigate to `APIs & Services` --> `Credentials` --> `Create credentials` --> `OAuth client ID`  

**NOTE**: *You might need to create `NEW PROJECT` if this is your first time and there are no projecte created yet.*  

With the new project created navigate to `APIs & Services` and click `ENABLE APIS AND SERVICES` and search for `Google+ API` and enable it.  

Then go to `Credentials` and click on `CREATE CREDENTIALS` and select `OAuth client ID`.  
*(If there is no consent screen created yet, create it by clicking on `CONFIGURE CONSENT SCREEN` and fill in the necessary fields.)*  

When thet is done select `Web application` as the application type.  
Customize the `Name` if needed.  

Add the following to the `Authorized redirect URIs`:

```text
http://127.0.0.1:8000/accounts/google/login/callback/
```
**NOTE**: *must be `127.0.0.1` and not `localhost` !!!*  
For further project deployment this will need to be changed to the actual domain name.  

Once you hit `Create` you will get the `client_id` and `secret_key` which you can use to fill in the fields in the django admin panel.  

Once the social application is created we can navigate to :  
`localhost:8000/accounts/login/`  
or  
`localhost:8000/accounts/signup/`  
and see the `Google` button which will redirect us to the Google login page.    

4. DONE!

## Adding authentication via 42 API:

1. **Installing necessary dependencies:**  

*(if not already installed)*

```bash
pipenv install requests

pipenv install PyJWT

pipenv install cryptography
```

...




## Some Documentation:

Django docs: [User authentication in Django](https://docs.djangoproject.com/en/5.0/topics/auth/)

How to use Django Widgets to style forms: [Django Widgets](https://docs.djangoproject.com/en/5.0/ref/forms/widgets/)  

3rd party authentication with Django: [allauth](https://docs.allauth.org/en/latest/)  


