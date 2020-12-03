### Fix to Werkzeug 1.0.x issue
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
###

import traceback
from api.log import log
from flask_restplus import Api

api = Api(version='1.0', title='Race Results API', description='An API that reads a race log file and calculates race results')


@api.errorhandler
def default_error_handler(e):
	message = 'An unhandled exception occurred.'
	log.exception(message)
	return {'message': message}, 500