from datetime import datetime

from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
from flask_socketio import SocketIO


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
        SECRET_KEY='amogus',
        MONGO_URI='mongodb://localhost:27017/chat-service',
        MONGO_USERNAME='root1',
        MONGO_PASSWORD='pass123456',
        MONGO_AUTH_SOURCE='admin'
    )


socketio = SocketIO(app)

mongodb_client = PyMongo(app)
db = mongodb_client.db


def messageRecieved(methods=['GET', 'POST']):
    print('Messsage received!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    db.chat.insert_one({'user': json['user_name'], 'text': json['message'], 'timeField': str(datetime.utcnow())})
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageRecieved)


@app.route("/add_one")
def add_one():
    db.chat.insert_one({'user': 'khan', 'text': 'abobus', 'timeField': str(datetime.utcnow())})
    return jsonify(message="success")


@app.route('/')
def sessions():
    return render_template('session.html')


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
