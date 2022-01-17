from flask import Flask, render_template, Response, jsonify, request, url_for, redirect, session
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
from flask_session import Session
# from flask_login import LoginManager, UserMixin, current_user, login_user, \
#     logout_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'P4bl0secret!key&ms4#1ñ2&%$Jaj4ja#ç'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
# login = LoginManager(app)
socketio = SocketIO(app, manage_session=False)

id_cliente = None


# class User(UserMixin, object):
#     def __init__(self, id=None):
#         self.id = id

# @login.user_loader
# def load_user(id):
#     return User(id)


@app.route('/', methods=["GET"])
def index():
    if request.method == "GET":
        return render_template('index.html')

@app.route('/chat', methods=["GET"])
def chat():
    if request.method == "GET":
        return render_template('chat.html')

@app.route('/botonera', methods=["GET"])
def botonera():
    if request.method == "GET":
        return render_template('botonera.html')

@app.route('/cliente', methods=["GET"])
def cliente():
    if request.method == "GET":
        return render_template('cliente.html')

@socketio.event
def id_Cliente():
    print(request.sid)
    join_room(request.sid)

# @socketio.event
# def connect():
#     emit('my_response', {'data': 'Connected'})

@socketio.event
def iniciarSession(data):
    session['nombre'] = data['nombre']
    emit('my_response', {'data': data['nombre']})

@socketio.event
def accion(data):
    sid = data.get('sid')
    emit('my_response', {'data': data['accion']}, room=sid)

@socketio.event
def mensaje(data):
    nombre = session.get('nombre') if session.get('nombre') else 'anonymous'
    emit('my_response', {'data': nombre + ': ' + data['message']}, broadcast=True)

@socketio.event
def join(message):
    join_room(message['room'])
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms())})

if __name__ == '__main__':
    socketio.run(app)