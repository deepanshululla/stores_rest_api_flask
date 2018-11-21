# REST API for E-Commerce Store on Containers

* Created a REST API with python flask and SQLALCHEMY as ORM using MySQL as the backend.
* Used docker compose for orchestrating python and MariaDB containers.
* Increased security by using JWT tokens for user authentication and authorization for specific requests.
* Used Postman for system testing and documenting the functionality of the REST API.
* Created unit,integration and system tests as well as makefile for test automation

## API is live on 
https://rest-api-stores-test.herokuapp.com

eg: To view list of items

https://rest-api-stores-test.herokuapp.com/items

eg: To view list of users

https://rest-api-stores-test.herokuapp.com/users



##  Clone it..
git clone https://github.com/deepanshululla/stores_rest_api_flask.git

git checkout docker

docker-compose up

## Docker images
https://hub.docker.com/r/deepanshululla/stores_rest_api/

docker pull deepanshululla/stores_rest_api

## API

### GET /users

This will return list of all users in json format. Passwords are not visible

### GET /items

This will return list of all items in json format

### GET /item/item-name

This will return a specific item requested by name.No 2 items can have unique name.(Requires JWT token for authentication and authorization
received via POST /auth). 

### POST /auth

This will generate a JSON Web Token(JWT) token for the username and password mentioned in json in the body.

### POST /item/item-name

This will create an item with the name in url and price mentioned in json.If the item already exists, this will fail.

### POST /register

This will create an user with the name and password mentioned in json.If the username already exists, this will fail

### PUT /item/item-name

This will create an item with the name in url and price mentioned in json.If the item already exists, this will update the price.

### DEL /item/item-name

This will delete an item with the mentioned name. If item doesn't exists it will fail.

### GET /store/store-name

This will return store with the mentioned name.No 2 stores can have same name. If store doesn't exists it will fail.

### POST /store/store-name

This will create a store with the name in url.If the store already exists, this will fail.

### DEL /store/store-name

This will delete store with the mentioned name. If store doesn't exists it will fail.

### GET /stores

This will return list of all stores in json format

## Sections

Section 3

* Rest(less) Flask API

Section 4

* Restful Flask API

Section 5 

* Flask API with SQLLITE backend

Section 6 

* Flask API with mysql backend

Section 7

* Flask API with SQLALCHEMY used as ORM

Section 8

* Adding stores resource and model to section 7.
