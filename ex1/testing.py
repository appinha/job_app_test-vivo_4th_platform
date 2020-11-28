from termcolor import colored
import numpy as np
from solution import *


def test(i, M, N, a, low, high, v=False):
	random_matrix = np.random.randint(low, high, (M, N))
	random_array = np.random.randint(low, high, (1, a))
	control_array = np.arange(high - low)
	control_res = count_arr_in_matrix(control_array, random_matrix)
	s = "Test {:>2}:".format(i)
	if control_res:
		control_sum = sum(list(map(int, control_res.split(', '))))
		if control_sum == random_matrix.size:
			print(colored(s, 'green'), "passed")
		else:
			print(colored(s, 'red'), "failed")
	else:
		print(colored(s, 'red'), "invalid input")
	if v:
		print(colored(" • Inputs:", 'blue'))
		print(random_matrix)
		print(random_array[0])
		print(colored(" • Answer:", 'blue'), count_arr_in_matrix(
				random_array[0], random_matrix))
		if control_sum:
			print(colored(" • Control:", 'yellow'),
					"{} vs {} (sum of counts vs qty of matrix elements)\n\
					".format(control_sum, random_matrix.size))

low = 0
high = 16
a = 3
i = 1

test(i, 2, 5, a, low, high, v=True)
i += 1

for N in range (2, 5):
	for M in range (2,5):
		test(i, M, N, a, low, high)
		i += 1

for N in range (2, 4):
	for M in range (2,4):
		test(i, 2, 5, a, 16, 20)
		i += 1
