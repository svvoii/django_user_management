# User Management Module for ft_transcendence

Django docs: [User authentication in Django](https://docs.djangoproject.com/en/5.0/topics/auth/)

### To setup the environment:

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


