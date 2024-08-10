# Name Generator

## Stack
* [Python 3.11](https://python.org/)
* [Mysql 5.7](https://www.mysql.com/)
* [Docker](https://www.docker.com/)

## Other Docs
* [Queries](./queries/README.md)
* [Controllers](./docs/CONTROLLERS.md)

## Setup Database
* Edit information as you please on: 
    *  _docker-compose.yaml_ and _config.json_
    * If it's necessary, update the _database-initilize.sh_ also
* Run docker compose 
```sh
docker compose up -d
```
* Run database initialize
```sh
./database-initialize --User --Password
```
* Now the DB is all set

## Setup python
```sh
python -m pip install -r requirements.txt
```