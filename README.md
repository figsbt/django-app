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
