Simple API for notes app, it has several end points for createing users and relevant notes.

Basicly it's just me playing with FastAPI inside a Docker file.
It's was writen to run on Azure App Service and SQL Server in Azure.

## Usage
The docker run command is:
```Dockerfile
docker run -d -p 1433:1433 -p 80:80 --name CONTAINER_NAME IMAGE_NAME
```

## TODOs- things I might want to add someday
[] Some sort of password security
[x] Dockerfile
[] Tests
