from termcolor import colored
import numpy as np
from solution import *


def test(i, M, N, a, low, high):
	random_matrix = np.random.randint(low, high, (M, N))
	random_array = np.random.randint(low, high, (1, a))
	control_array = np.arange(high - low)
	control_res = ""

	#print(colored("\nInputs:", 'blue'))
	#print(random_matrix)
	#print(random_array[0])
	#print(colored("Answer:", 'blue'), count_arr_in_matrix(random_array[0], random_matrix))
	control_res = count_arr_in_matrix(control_array, random_matrix)
	if (control_res and sum(list(map(int, control_res.split(', ')))) == random_matrix.size):
		print(colored("Test", 'green'), colored(i, 'green'), colored(":", 'green'), "passed")
	else:
		print(colored("Test", 'red'), colored(i, 'red'), colored(":", 'red'), "failed")


a = 3
i = 1

for N in range (2, 5):
	for M in range (2,5):
		test(i, M, N, a, 0, 16)
		i += 1

for N in range (2, 4):
	for M in range (2,4):
		test(i, 2, 5, a, 16, 20)
		i += 1

print("")