# Corgree Challenge
Corgee REST API App 

## To run the app on docker:
- Clone the repo to your local
- cd into folder.
- Create .env file ---> You can copy .env.example then rename and edit it.
- Run the following command: `docker-compose up --build -d`  (this will build the docker services and run it in background)
- To check the status of the running containers, run the following command `docker ps -a`
- To get inside the docker container using this: `docker exec -u 0 -it Container_ID bash`
- To create super user inside docker `./manage.py createsuperuser`
- Make migrations: `./manage.py makemigrations`
- Migrate: `./manage.py migrate`
- ...

### To restart the server:
- Run the server: `./manage.py runserver` or restart the "api" container `docker restart Container_ID`

......

### To check the endpoints by url
- List all users and register new user
`http://localhost:3000/api/users/register`
`http://localhost:3000/api/users/login`
`http://localhost:3000/api/users/logout`
...

- List all Transactions , Add 
`http://localhost:3000/api/transactions`
..
- Update or Delete  (You must be authenticated first)
`http://localhost:3000/api/transactions/{id}`

`ps: you can disable auth for development purposes from settings.py file --> hash line 64 `
...


### Tests:
-- To be added ..


### Application using: 
- Django: 3.1.4
- djangorestframework --> for rest api 
- djangorestframework-simplejwt --> for login tokens
- PyMySQL --> for the connection mysql and python
