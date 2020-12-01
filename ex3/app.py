from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import json
from parse_log import get_race_res

# Instantiate a Flask object (the application)
app = Flask(__name__)


def get_race_res_json(file):
	'''
		This function gets race results from log file, then converts it to JSON.
		The return is JSON-like dicts of the dataframes containing the results.
	'''
	# Get race results
	df_res, df_best_lap = get_race_res(file)
	# Convert dataframes to JSONlike dicts
	json_race_res = json.loads(df_res.to_json(orient="split"))
	json_best_lap = json.loads(df_best_lap.to_json(orient="split"))
	return json_race_res, json_best_lap


# Endpoint for posting API's log input
@app.route('/post', methods=['POST'])
def post():
	'''
		This function gets the posted log file, then gets race results.
		The return is a JSON representation of the result dataframes.
	'''
	file = request.files['file']
	race_res = get_race_res_json(file)
	return jsonify(race_res)


# Route for visualizing the results
@app.route('/')
def show_results():
	'''
		This function gets race results from log file, then converts it to JSON.
		The result dataframes are then rendered as HTML tables.
	'''
	df_res, df_best_lap = get_race_res("corrida.log")
	return render_template('view.html', \
		tables=[df_res.to_html(classes='results'), \
		df_best_lap.to_html(classes='results')], \
			titles=['na', 'Resultados Gerais', 'Melhor Volta da Corrida'])


if __name__ == '__main__':
	app.run(debug=True)