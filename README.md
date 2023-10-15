# Django App | BackendAssignment


    
## Assignment Checklist 
1. Create a Django project named "BackendAssignment."                 | :heavy_check_mark: 
2. Develop a Django app within the project called "api."              | :heavy_check_mark: 
3. Create two models named "User" and "Post".                         | :heavy_check_mark: 
   with appropriate fields and relationships between them.            | :heavy_check_mark: 
   Ensure that the User model includes fields for authentication.     | :heavy_check_mark: 
4. APIs for user-registration, auth(JWT tockens), posting new content.| :heavy_check_mark: 
5. Authorisation to ensure only authenticated-users can create posts. | :heavy_check_mark: 
6. Configure the Django project to use PostgreSQL as DB.              | :heavy_check_mark: 


## Design
* Django web app to serve user-create, user-login and create-post APIs                   | [api-app-urls](BackendAssignment/api/urls.py)
* User and Post Models as described here with required fields (includes authentication)  | [api-app-models](BackendAssignment/api/models.py)
* The django-app is containarized along with Postgres image and run via docker-compose   | [docker-compose](docker-compose.yml)
* The setup is of single node right now, have detailed on how to scale the above setup for performance and scale in a section below.


## How to setup and test the APIs
* Working directory    : [django-app](.)
* Set ENV variables    : `export DB_NAME=postgres DB_USER=postgres DB_PASSWORD=bap1er DB_HOST=pgsqldb DB_PORT=5432 SECRET_KEY=fl^r%j9l@zev APP_WORKERS=2`
* Build docker compose : `docker compose build`
* Start docker compose : `docker compose up -d`
* Stop docker compose  :
    - `docker compose down -v` # to remove volumes too
    - `docker compose down` # to retain state of postgres


---

Testing the APIs 

* via cURL

```
1. Create User API : An API endpoint to create a new User
    - Request
        - curl --location 'http://127.0.0.1:8000/api/create-user' --header 'Content-Type: application/json' --data-raw '{ "email_id": "user1@email.com", "password": "ashaR3!er", "full_name": "My Name" }'
    - Response
        - {"Message": "User account created successfully for user1@email.com"}
```

```
2. Login User API: An API endpoint to login; which returns an JWT token for Authorization
    - Request
        - curl --location 'http://127.0.0.1:8000/api/login-user' --header 'Content-Type: application/json' --data-raw '{"email_id": "user1@email.com", "password": "ashaR3!er"}'
    - Response
        - {"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXIxQGVtYWlsLmNvbSJ9.cM7hr3Mm2wmzz6m7NO928Vl-I7JSBMQpdTN2058YXnI"}
```

```
3. Create Post API: An API endpoint to create a Post only if authenticated via a valid JWT token
    - Request
        - curl --location 'http://127.0.0.1:8000/api/create-post' --header 'Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXIxQGVtYWlsLmNvbSJ9.cM7hr3Mm2wmzz6m7NO928Vl-I7JSBMQpdTN2058YXnI' --header 'Content-Type: application/json' --data '{"post_content": "NASA experts wanted India to share space technology after seeing Chandrayaan-3 craft development: ISRO chief Somanath"}'
    - Response
        - {"Message": "Post created successfully!"}
```

* postman-collection is attached in the email

---

## How to scale this. A short note.

    - Any RDBMS(PostgresSQL here) should be a muti-node distributed setup. 
        - Data sharded across the nodes for better performance
        - Each primary shard with a replica for high availability
        - Something like this (https://vitess.io/) to scale MySQL

    - As the web-app itself is containarized, it can be deployed on kubernetes to scale on demand.


## Good to haves (But couldn't add because of lack of time)
    - 100% test coverage
    - CICD and tests part of CI step
    - The secrets are exposed as part of README but ideally, they should be pulled on-fly from a secret store like Vault etc.
