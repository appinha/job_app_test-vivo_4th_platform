import pandas as pd
import numpy as np
from datetime import timedelta

log_file = "corrida.log"

# Read log file and put it into pandas dataframe
df_log = pd.read_csv(log_file, delimiter=';', \
			dtype={'Velocidade média da volta': str})

# Split 'Super-Heroi' column into two (to separate code from name)
codes = []
names = []
for string in df_log['Super-Heroi']:
	a, b = map(str, string.split('–'))
	codes.append(a)
	names.append(b)

# Reorder dataframe columns
df_log_ord = pd.DataFrame({'Codigo': codes, \
							'Super-Heroi': names, \
							'Hora': df_log['Hora'], \
							'Nº Volta': df_log['Nº Volta'], \
							'Tempo Volta': df_log['Tempo Volta'], \
							'Velocidade média da volta': \
								df_log['Velocidade média da volta']})

# List all unique super-hero codes and names
code_unique = df_log_ord['Codigo'].unique()
name_unique = df_log_ord['Super-Heroi'].unique()

# Function to convert string with time to seconds in float
def time_sum(lst):
	mins, secs = map(float, lst.split(':'))
	td = timedelta(minutes=mins, seconds=secs)
	return td.total_seconds()

# Get total race time for each super-hero
times = []
best_time = []
for code in code_unique:
	# Filter dataframe per super-hero code (row) and lap time (column)
	df_filt_time = df_log_ord['Tempo Volta'].loc[df_log_ord['Codigo'] == code]
	# Convert string with time to seconds in float
	df_filt_time = df_filt_time.apply(time_sum)
	# Find best lap time (bonus)
	best_time.append(df_filt_time.min())
	# Populate list with sum of lap times
	times.append(df_filt_time.sum())

# Find best lap time of all super-heros (bonus)
best_time_all = name_unique[best_time.index(min(best_time))]

# Get average speed for each super-hero
avg_speed = []
code = 0
for code in code_unique:
	# Filter dataframe per super-hero code (row) and lap average speed (column)
	df_filt_speed = df_log_ord['Velocidade média da volta'].loc[df_log_ord['Codigo'] == code]
	# Replace comma for point in string list, then convert to float
	speeds_f = []
	for s in df_filt_speed:
		speeds_f.append(float(s.replace(',', '.')))
	# Calculate average of list with lap average speeds
	avg_speed.append(sum(speeds_f) / len(speeds_f))

# Get total laps for each super-hero
df_counts = df_log_ord['Codigo'].value_counts()

# Create index with unique super-hero codes for race results dataframe
idx = pd.Index(code_unique, name='Codigo')

# Create dict with calculated race results
data = {'Super-Heroi': name_unique, \
		'Qtd Voltas': df_counts, \
		'Tempo Total (s)': times, \
		'Melhor Volta (s)': best_time, \
		'Velocidade média': avg_speed}

# Unite index and data dict to create race results dataframe
df_res = pd.DataFrame(data, index=idx)

# Sort dataframe by position
df_res = df_res.sort_values(by=['Tempo Total (s)'])

# Add column for finishing position
df_res['Posicao Chegada'] = np.arange(1, len(code_unique) + 1)

print(df_res)
print("\nMelhor volta da corrida:", best_time_all)