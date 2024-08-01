# Author: Max Resch

#--------------------------------------------------
# Import Requirements
#--------------------------------------------------
import os
from flask import Flask
from flask_socketio import SocketIO
from flask_failsafe import failsafe
from flask_cors import CORS

socketio = SocketIO()

#--------------------------------------------------
# Create a Failsafe Web Application
#--------------------------------------------------
@failsafe
def create_app(debug=False):
	app = Flask(__name__)
	CORS(app)

	# This will prevent issues with cached static files
	app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
	app.config['CORS_HEADERS'] = 'Content-Type'
	app.debug = debug
	# The secret key is used to cryptographically-sign the cookies used for storing the session data.
	app.secret_key = 'AKWNF1231082fksejfOSEHFOISEHF24142124124124124iesfhsoijsopdjf'
	# ----------------------------------------------

	from .database.database import database
	db = database()
	db.createTables(purge=True)
	
	
	# This will create a user
	db.createUser(email='owner@email.com' ,password='password', role='owner')
	db.createUser(email='guest@email.com' ,password='password', role='guest')
	# ----------------------------------------------

	socketio.init_app(app)

	with app.app_context():
		from . import routes
		return app
