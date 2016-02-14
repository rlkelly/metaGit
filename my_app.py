from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    print socket.gethostbyname(socket.gethostname())
    app.run(host= '0.0.0.0')

