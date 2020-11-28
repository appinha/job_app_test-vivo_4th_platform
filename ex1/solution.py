import numpy as np

def count_arr_in_matrix(array, matrix):
	"""
		This function takes in a 1D array and a 2D array (matrix). It counts
		how many times each array element occurs in the matrix. The return is a
		space-comma string with occurrence counts.
	"""
	res = []

	# Check input conditions, i.e. if elements are in range(16).
	if np.all((matrix >= 0) & (matrix <= 15)) and \
		np.all((array >= 0) & (array <= 15)) :
		for i in range(len(array)):
			res.append(np.count_nonzero(matrix == array[i]))
		return ', '.join(map(str, res))
