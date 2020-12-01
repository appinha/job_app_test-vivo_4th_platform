import pandas as pd
import numpy as np
from datetime import timedelta


# Function to convert string with time to in float representing seconds
def time_sum(lst):
	'''
		This function takes in a string with time in format M:S.MS and converts
		it to a float in format S.MS.
		The return is the converted time in float.
	'''
	mins, secs = map(float, lst.split(':'))
	td = timedelta(minutes=mins, seconds=secs)
	return td.total_seconds()


def get_race_res(log_file):
	'''
		This function takes in a file with a race log and calculate its results.
		The returns are 2 dataframes: general race results and best race lap.
	'''

	# Read log file and put it into pandas dataframe
	df_log = pd.read_csv(log_file, delimiter=';')

	# List all unique super-hero code-name
	code_name_unique = df_log['Super-Heroi'].unique()

	# Split code-name (to separate code from name)
	code_unique = []
	name_unique = []
	for unique in code_name_unique:
		a, b = map(str, unique.split('–'))
		code_unique.append(a)
		name_unique.append(b)

	# Get total race time and best lap time for each super-hero
	total_race_time = []
	best_lap_time = []
	best_lap_time_nbr = []
	for code in code_name_unique:
		# Filter dataframe rows per super-hero in lap time column
		df_filt_time = df_log['Tempo Volta'].loc[df_log['Super-Heroi'] == code]
		# Convert time (in string) to seconds (in float)
		df_filt_time = df_filt_time.apply(time_sum)
		# Find best lap time (bonus)
		best_lap_time.append(df_filt_time.min())
		# Get number of best lap time (bonus)
		blt_index = df_filt_time[df_filt_time == df_filt_time.min()].index[0]
		best_lap_time_nbr.append(df_log['Nº Volta'].iloc[blt_index])
		# Populate list with sum of lap times
		total_race_time.append(df_filt_time.sum())

	# Find best lap time of all super-heros (bonus)
	best_lap_time_all_name = name_unique[best_lap_time.index(min(best_lap_time))]

	# Get average speed for each super-hero
	avg_speed = []
	code = 0
	for code in code_name_unique:
		# Filter dataframe per super-hero code (row) and lap average speed (column)
		df_filt_speed = df_log['Velocidade média da volta'].loc[df_log['Super-Heroi'] == code]
		# Replace comma for point in string list, then convert to float
		speeds_f = []
		for s in df_filt_speed:
			speeds_f.append(float(s.replace(',', '.')))
		# Calculate average of list with lap average speeds
		avg_speed.append(sum(speeds_f) / len(speeds_f))

	# Get total laps for each super-hero
	df_counts = df_log['Super-Heroi'].value_counts()

	# Create index with unique super-hero codes for race results dataframe
	idx = pd.Index(code_name_unique)

	# Create dict with calculated race results
	data = {'Codigo': code_unique, \
			'Super-Heroi': name_unique, \
			'Qtd Voltas': df_counts, \
			'Tempo Total (s)': total_race_time, \
			'Melhor Volta': best_lap_time_nbr, \
			'Tempo Melhor Volta (s)': best_lap_time, \
			'Velocidade média': avg_speed}

	# Unite index and data dict to create race results dataframe
	df_res = pd.DataFrame(data, index=idx)

	# Get dataframe columns for reordering it later
	cols = list(df_res.columns.values)
	cols.insert(0, 'Posição Chegada')

	# Sort dataframe by position
	df_res = df_res.sort_values(by=['Tempo Total (s)'])

	# Add column for finishing position into sorted dataframe
	df_res['Posição Chegada'] = np.arange(1, len(code_name_unique) + 1)

	# Reorder dataframe columns
	df_res = df_res[cols]

	# Populate dict with info of best lap time in race
	bl_index = (df_res['Codigo'].loc[df_res['Super-Heroi'] == best_lap_time_all_name].index[0])
	best_lap = {'Tempo Melhor Volta (s)': \
		[df_res['Tempo Melhor Volta (s)'].loc[df_res['Super-Heroi'] == \
			best_lap_time_all_name].item()]}
	df_best_lap = pd.DataFrame(best_lap, index=[bl_index])

	return df_res, df_best_lap
