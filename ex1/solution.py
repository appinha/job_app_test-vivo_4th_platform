## SUBJECT
# Uma imagem bitmap pode ser representada como uma matriz de dimensões
# M x N, em que cada posição da matriz pode assumir um valor inteiro dentro de
# um intervalo. Construa um algoritmo que receba como entrada um Vetor A[N]
# em que An ∈ { 0, 1, 2,..., 15 }. A saída do seu algoritmo deve ser uma String
# indicando a quantidade de vezes que cada An foi encontrado na matriz de
# bitmap. No caso em que algum elemento não tenha sido encontrado, o
# algoritmo deve retornar que a quantidade é zero para aquele elemento. O
# formato da String é livre.

import numpy as np

def count_arr_in_matrix(array, matrix):
	res = []

	if np.all((matrix >= 0) & (matrix <= 15)) and \
		np.all((array >= 0) & (array <= 15)) :
		for i in range(len(array)):
			res.append(np.count_nonzero(matrix == array[i]))
		return ', '.join(map(str, res))
