# ABRED

AI-Bigdata based REconstruction/redevelopment Decision support system

## Overview

Sample program to build MySQL and Fast API environment with DockerCompose

## Install

Create and Running

add `.env` file and add configs

```
# .env example

MYSQL_DATABASE=fastapi
MYSQL_USER=user
MYSQL_PASSWORD=password
MYSQL_ROOT_PASSWORD=password
MYSQL_HOST=db

NEWS_CLIENT_ID = OsLOua238f8IXy9nanMl #naver
NEWS_CLIENT_PW = GTaGmO7nii
CONSTRUCTION_SERVICE_KEY = 457570424d6b756e36376345746541 #cleanup.seoul.go.kr
GEOCODING_SERVICE_KEY=5DCD1A9F-FEB6-3DF0-9AD5-433C6D1D5155 #https://www.vworld.kr/dev/v4dv_geocoderguide2_s001.do


```

run docker-compose

```
$ make up
```


## DB migration  
before migration, fix fastapi code

```
# access fastapi docker
$ docker exec -it fastapi /bin/bash

# inside of fastapi docker
# move to src directory
> cd ..

# run migration
> alembic upgrade head

```
When change model.py(table description)

```
# Please check table are well defined, and mysql db connection is correct.

# Please check your alembic head by 'alembic log'. If not, try 'alembic upgrade' until proper commit

# make auto-generate alembic revision
> alembic revision --autogenerate -m "message"

# after make revision, please check carefully, that the revision is correct. If not, correct it.

# run migration
> alembic upgrade head 
```

## Construction data dump
TODO


