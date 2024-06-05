# User Management Module for ft_transcendence

### To setup the environment for the project:

#### ON LINUX:

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


#### ON MACOS (M1):

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

### Setting Up POSTGRESQL:

#### Setting up PostgreSQL database with Heroku (cloud service):

1. Create an account on Heroku.

```bash
https://www.heroku.com/

https://id.heroku.com/login

email@email.com
'passsword'
```

2. Create a new app on Heroku.

```bash
https://dashboard.heroku.com/apps

New -> Create new app
```
**NOTE**: ..was free to create a new app.. free no more..

... gonna change the steps to use local postgresql database...


## Some Documentation:

Django docs: [User authentication in Django](https://docs.djangoproject.com/en/5.0/topics/auth/)

How to use Django Widgets to style forms: [Django Widgets](https://docs.djangoproject.com/en/5.0/ref/forms/widgets/)  

3rd party authentication with Django: [allauth](https://docs.allauth.org/en/latest/)  


