from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from parse_log import get_race_res_json

# Instantiate a Flask object (the application)
app = Flask(__name__)

# Endpoint for posting API's log input
@app.route('/post', methods=['POST'])
def post():
	'''
		This function gets the posted log file,
	'''
	file = request.files['file']
	race_res = get_race_res_json(file)
	return jsonify(race_res)

if __name__ == '__main__':
	app.run(debug=True)