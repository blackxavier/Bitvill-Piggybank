# Bitvill-Piggybank

## What is this API is used for

This API is used to store transactions which can be grouped into categories. It is a modification of a tutorial by Vitor Freitas on DRF . [Visit Tutorial](https://youtube.com/playlist?list=PLLxk3TkuAYnrO32ABtQyw2hLRWt1BUrhj). I modified my version by using both class and function based views since he used *ModelViewSet*. I also added some additional views and serializers.

### Authentication
To accesss endpoints, a client has to register using the following details
* email
* password
* confirm_password


This parameters should be passed via a *POST* request to *api/auth/register/*
Upon successfull request a token would be recieved.

To login use the following details
* email
* password
This parameters should be passed via a *POST* request to *api/auth/login/*
Upon successfull request a token would be recieved.


