## US Stock Market daily Prices ![Django](https://img.shields.io/badge/Django-2.2.9-yellow.svg)

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Run](#run)

## General info
- This project let's you see the daily chart for any share in the US stock market, You can see the [High,Low,Open,Close] prices for each day on the chat.
- The prices are from Alphavantage-API and we make a request with the share we want to know info about and then get json response.
- There is also an API built for this application that return the daily prices for the last 100 days from our database

## Technologies
Project is created with:
* Django: 2.2
* Django Rest Framework
	
## Run
To run this project, install it locally and run this command

```
$ pip install -r requirements.txt
$ python manage.py runserver
```
