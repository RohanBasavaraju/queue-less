# Queue-less (QLess)
Queue-less is a mobile app bringing you the shortest wait times for local restaurants, supermarkets, food banks, and more.

This project will be submitted for Cal Hacks 2020 to serve as a platform helping those afflicted by the COVID-19 pandemic.

# Backend 

The backend was done in python and googlemaps, sqlalchemy, requests libraries.

We created a simple database that can store information of grocery stores and their traffics (i.e. number of people there in every hour). 

We also created some REST APIS that enable putting in data and retrieving information from the database.

Also, some utility functions were implemented as the part of the desired business logic: we can find the current location of the device, find the nearby stores based on a keyword, calculate the distance to those stores and find the best one to go.

