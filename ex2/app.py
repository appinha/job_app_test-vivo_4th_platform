import sys
sys.path.append('../ex1')
from flask import Flask, request, jsonify
from flask_restful import reqparse
import numpy as np
from solution import *

# Instantiate a Flask object (the application)
app = Flask(__name__)

# Generate matrix with random values in range (16)
matrix = np.random.randint(0, 16, (2, 2))

# Endpoint for posting API's JSON input
@app.route('/post', methods=['POST'])
def post():
	'''
		This function parses the posted JSON file and converts it to a numpy
		1D array; it then checks if array values are in valid range; if so, it
		calls count_arr_in_matrix() and its result is put into a python dict.
		The return is a JSON representation of the dict containing the result.
	'''
	parser = reqparse.RequestParser()
	parser.add_argument('list', action='append')
	parser = parser.parse_args()
	array = np.array(list(map(int, parser['list'])))
	if all(i >= 0 and i <= 15 for i in array):
		count = count_arr_in_matrix(array, matrix)
		res = {"counts": count}
		return jsonify(res)
	else:
		return 'Please provide list values in range 0 <= value <= 15.\n'

if __name__ == '__main__':
	app.run(debug=True)