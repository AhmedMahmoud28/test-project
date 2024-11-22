# Invoice_BE

Creating simple API Endpoints

# Setup

first run these in your terminal

```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8
sudo apt install python3.8-venv
sudo apt-get install python3.8-dev
sudo apt-get install python-setuptools
sudo apt-get install build-essential python3.8-dev
```

then run this command after changing directory to your project directory

```
python3.8 -m venv env

```

this command will activate virtual environment for your project and you will have to install requirements for your project inside environment by running this

```
pip install -r requirements.txt
```

Create .env file on this repo and provide secret key and debug for the project

```
SECRET_KEY=gfsgajgajlgkemfl
DEBUG=True
```

then run these command to start using development server

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Usage

Use the post endpoint to add invoice with its details, In put endpoint I made assumption that I would need to either delete an invoice detail or edit it
so that in put endpoint you have to send the same details again if you want to keep them or send one if you want to delete the other

# note

* Swagger is provided
