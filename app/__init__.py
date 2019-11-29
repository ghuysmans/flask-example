from flask import Flask

app = Flask(__name__)
if app.config['DEBUG']:
    #disable caching
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

from app import routes
