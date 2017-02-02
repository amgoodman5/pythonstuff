from flask import Flask

import models
from resources.cats import cats_api


DEBUG = True
HOST = '0.0.0.0'
PORT = 8000

app = Flask(__name__)
app.register_blueprint(cats_api)


@app.route('/')
def hello_world():
    return 'Hello World 2'

if __name__ ==  '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
