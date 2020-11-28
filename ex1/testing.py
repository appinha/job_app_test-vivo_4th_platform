from termcolor import colored
import numpy as np
from solution import *


def test(i, M, N, a, low, high, v=False):
	"""
		This function tests the count_arr_in_matrix() function.

		It takes in six integers: test numbering (i), matrix dimensions (M, N),
		array length (a) and range (low, high). The boolean "v" is for verbose.
		It generates a 1D and a 2D arrays with random values within given range.
		It also generates a control array with all values within this range.

		To check if the function is correctly counting occurrences, the control
		array is used to return counts of all values in matrix. Thus, the sum of
		these counts is compared with the quantity of elements in the matrix,
		which should be equal if function works correctly.

		There is no return value, the test result is simply printed in stdout.
		Possible test results: "passed", "failed" and "invalid input".
	"""
	random_array = np.random.randint(low, high, (1, a))
	random_matrix = np.random.randint(low, high, (M, N))
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

# Verbose testing with correct input
test(i, 2, 5, a, low, high, v=True)
i += 1

# Correct input testing
for N in range (2, 5):
	for M in range (2,5):
		test(i, M, N, a, low, high)
		i += 1

# Incorrect input testing
for N in range (2, 4):
	for M in range (2,4):
		test(i, 2, 5, a, 16, 20)
		i += 1
