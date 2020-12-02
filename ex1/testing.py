from termcolor import colored
import numpy as np
from solution import count_arr_in_matrix


### TO CHANGE TESTING PARAMETERS, EDIT VARIABLE VALUES BELLOW

## CORRECT INPUT TESTING
# 1D array length
a = 3
# Range of matrix dimensions (MxN)
d_low = 2
d_high = 5

## INCORRECT INPUT TESTING
# 1D array length
i_a = 3
# Range of arrays' elements
i_low = 16
i_high = 20
# Range of matrix dimensions (MxN)
i_d_low = 2
i_d_high = 4



def test(i, M, N, a, low, high, v=False):
	'''
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
		Possible test results: "passed" and "failed".
	'''
	random_array = np.random.randint(low, high, (1, a))
	random_matrix = np.random.randint(low, high, (M, N))
	control_array = np.arange(low, high)
	control_res = count_arr_in_matrix(control_array, random_matrix)
	title = "Test {:>2}:".format(i)

	if control_res:
		control_sum = sum(list(map(int, control_res.split(', '))))
		if control_sum == random_matrix.size:
			print(colored(title, 'green'), "passed")
		else:
			print(colored(title, 'red'), "failed")

	if v:
		print(colored(" • Inputs:", 'blue'), "matrix,", colored("array", 'cyan'))
		print(random_matrix)
		print(colored(random_array[0], 'cyan'))
		print(colored(" • Answer:", 'blue'), count_arr_in_matrix(
				random_array[0], random_matrix))
		if control_sum:
			print(colored(" • Control:", 'yellow'),
					"{} vs {}\n   (sum of counts vs qty of matrix elements)\
					".format(control_sum, random_matrix.size))


# Testing numbering
i = 1
# Range - correct input
low = 0
high = 16

# Verbose testing with correct input
print(colored("\n--- Correct input testing - verbose mode ---", 'magenta'))
test(i, 3, 5, 5, low, high, v=True)
i += 1

# Correct input testing
print(colored("\n--- Correct input testing ---", 'magenta'))
for N in range (d_low, d_high):
	for M in range (d_low, d_high):
		test(i, M, N, a, low, high)
		i += 1

# Incorrect input testing
print(colored("\n--- Incorrect input testing ---", 'magenta'))
for N in range (i_d_low, i_d_high):
	for M in range (i_d_low, i_d_high):
		test(i, M, N, i_a, i_low, i_high)
		i += 1

print("")