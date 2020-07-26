import os
import json

from flask import Flask, request
from sqlalchemy import create_engine

app = Flask(__name__)

config = {
    'DATABASE_URI': os.environ.get('DATABASE_URI', ''),
    'HOSTNAME': os.environ['HOSTNAME'],
    'GREETING': os.environ.get('GREETING', 'Bambaleilo'),
}
engine = create_engine(config['DATABASE_URI'], echo=True)

@app.route("/health")
def health():
    return '{"status": "Ok"}'

@app.route("/version")
def version():
    return '{"version": "Skaffold"}'

@app.route("/")
def Bambaleilo():
    return 'Hello world from ' + os.environ['HOSTNAME'] + '!'

@app.route("/config")
def configuration():
    return json.dumps(config)

@app.route('/db')
def db():
    rows = []
    with engine.connect() as connection:
         result = connection.execute("select id, name from client;")
         rows = [dict(r.items()) for r in result]
    return json.dumps(rows)


# Add new user
@app.route('/user', methods=['POST'])
def add_user():
    id = request.json['id']
    name = request.json['name']

    with engine.connect() as connection:
         connection.execute("insert into client(id, name) values ({id}, '{name}');")
    return "new user {name} added"

# Get user
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    rows = []
    engine = create_engine(config['DATABASE_URI'], echo=True)
    with engine.connect() as connection:
        result = connection.execute("select * from client where id = {id};")
        rows = [dict(r.items()) for r in result]
    return json.dumps(rows)

# Update user
@app.route('/user', methods=['PUT'])
def update_user():
    id = request.json['id']
    username = request.json['name']

    with engine.connect() as connection:
        connection.execute("update client set name = '{name}' where id = {id};")
    return "user {name} updated"

# Delete user
@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    with engine.connect() as connection:
        connection.execute("delete from client where id = {id};")

    return "user {id} deleted"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')