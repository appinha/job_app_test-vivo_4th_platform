from flask import request, jsonify, render_template, make_response
from flask_restplus import Resource
from werkzeug.utils import secure_filename
from api.restplus import api
from api.parse_log import get_race_res, get_race_res_json

race_res = api.namespace('results', description='Race Results')

# Endpoint for posting API's log input
@race_res.route('/post', methods=['POST'])
class Post(Resource):
	def post(self):
		'''
			This function gets the posted log file, then gets race results.
			The return is a JSON representation of the result dataframes.
		'''
		file = request.files['file']
		json_res = get_race_res_json(file)
		return jsonify(json_res)


# Endpoint for visualizing the results
@race_res.route('/', methods=['GET'])
class ShowResults(Resource):
	def get(self):
		'''
			This function gets race results from log file, then converts it to JSON.
			The result dataframes are then rendered as HTML tables.
		'''
		headers = {'Content-Type': 'html'}
		df_res, df_best_lap = get_race_res("corrida.log")
		return make_response(render_template('view.html', \
			tables=[df_res.to_html(classes='results'), \
			df_best_lap.to_html(classes='results')], \
				titles=['na', 'Resultados Gerais', 'Melhor Volta da Corrida']))
