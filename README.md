# Flask Rest APIs

### GET /users

This will return list of all users in json format. Passwords are not visible

### GET /items

This will return list of all items in json format

### GET /item/<item-name>

This will return a specific item requested by name.No 2 items can have unique name.(Requires JWT token). 

### POST /auth

This will generate a JWT token for the username and password mentioned in json in the body.

### POST /item/<item-name>

This will create an item with the name in url and price mentioned in json.If the item already exists, this will fail.

### POST /register

This will create an user with the name and password mentioned in json.If the username already exists, this will fail

### PUT /item/<item-name>

This will create an item with the name in url and price mentioned in json.If the item already exists, this will update the price.

### DEL /item/<item-name>

This will delete an item with the mentioned name. If item doesn't exists it will fail.


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
