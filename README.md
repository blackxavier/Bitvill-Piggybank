# Bitvill-Piggybank

## What is this API  used for

This API is used to store transactions which can be grouped into categories. It is a modification of a tutorial by Vitor Freitas on DRF [Visit Tutorial](https://youtube.com/playlist?list=PLLxk3TkuAYnrO32ABtQyw2hLRWt1BUrhj). I modified my version by using both class and function based views since he used *ModelViewSet*. I also added some additional views and serializers.

## API Endpoints

### Users

* auth/register/ - (registers users)
* auth/login/ - (logs in users)
* logout/ - (logs out users)
* change-password/ - (change users password)
* me/ - (view users information)

### Currencies

* currencies/ - (view all currencies)

### Category

* categories/ - (view all categories)
* categories/id/ - (view/edit/update/delete single category)
* me/categories/delete/ - (delete all categories)

### Transactions

* transactions/  - (view all transactions)
* transactions/id/  - (view/edit/update/delete single transaction)
* me/transactions/delete/  - (delete all transactions)

### Install

## Clone repository

    Clone repository - git clone https://github.com/blackxavier/Bitvill-Piggybank.git

## Create virtual environment and install requirements 

    Create a virtual environment - virtualenv env
    Install requirements - pip install -r requirements.txt

## Migrate and run server

    Make migrations - py manage.py makemigrations
    Migrate - py manage.py migrate
    Create superuser - py manage.py createsuperuser
    Launch server - py manage.py runserver 
    Log in to admin
