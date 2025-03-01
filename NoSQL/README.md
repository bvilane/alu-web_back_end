# NoSQLProject

# MongoDB List Databases

This project provides scripts to list all databases in MongoDB.

## Requirements

- Ubuntu 18.04 LTS
- MongoDB 4.2
- Python 3.7
- PyMongo 3.10

## Installation

1. Install MongoDB 4.2:
    ```sh
    $ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
    $ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
    $ sudo apt-get update
    $ sudo apt-get install -y mongodb-org
    ```

2. Start MongoDB service:
    ```sh
    $ sudo service mongod start
    ```

3. Install PyMongo:
    ```sh
    $ pip3 install pymongo
    ```

## Usage

### MongoDB Shell Script

To list all databases using the MongoDB shell script, run:
```sh