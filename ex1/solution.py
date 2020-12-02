import numpy as np

def count_arr_in_matrix(array, matrix):
	'''
		This function takes in a 1D array and a 2D array (matrix). It counts
		how many times each array element occurs in the matrix.
		The return is a comma-space delimited string with occurrence counts.
	'''
	res = []

	# Check input conditions, i.e. if array elements are in range(16).
	if not np.all((array >= 0) & (array <= 15)):
		raise Exception("Please provide values within range [0, 15]")
	# Count occurrences of array elements in matrix
	for i in range(len(array)):
		res.append(np.count_nonzero(matrix == array[i]))
	# Convert the counting into a comma-space delimited string
	return ', '.join(map(str, res))
