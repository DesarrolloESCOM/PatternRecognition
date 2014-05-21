__author__ = 'alberto'
from random import choice

#import matplotlib.pyplot as plt

from numpy import array, dot, random

import numpy as np
import matplotlib.pyplot as plt

def perceptronOR():
	unit_step = lambda x: 0 if x < 0 else 1
	training_data = [
		(array([0,0,1]), 0),
		(array([0,1,1]), 1),
		(array([1,0,1]), 1),
		(array([1,1,1]), 1), ]
	w = random.rand(3)
	errors = []
	eta = 0.2
	n = 100
	for i in xrange(n):
		x, expected = choice(training_data)
		result = dot(w, x)
		error = expected - unit_step(result)
		errors.append(error)
		w += eta * error * x
		for x, _ in training_data:
			result = dot(x, w)
			#print("{}: {} -> {}".format(x[:2], result, unit_step(result)))
	valores = []
	for x in xrange(5):
		valores.append((w[2]*x+w[1]*x+w[0]*x))
	print valores #plt.plot(valores)
	#plt.show()
def dot_product(values, weights):
	return sum(value * weight for value, weight in zip(values, weights))


def perceptronWIKI():
	threshold = 0.5
	learning_rate = 0.001
	weights = [0, 0, 0]
	training_set = [
		((1, 0, 0), 0),
		((1, 0, 1), 1),
		((1, 1, 1), 1),
		((1, 1, 1), 1)
	]
	while True:
		#print('-' * 60)
		error_count = 0
		for input_vector, desired_output in training_set:
			#print(weights)
			result = dot_product(input_vector, weights) > threshold
			error = desired_output - result
			if error != 0:
				error_count += 1
				for index, value in enumerate(input_vector):
					weights[index] += learning_rate * error * value
		if error_count == 0:
			break
	print weights

def perceptronPractica():
	threshold = 0.5
	learning_rate = 0.001
	weights = [1, 1, 1, 1]
	"""
	x1 = np.asarray([[0, 1, 1, 1], [0, 0, 0, 1], [0, 1, 0, 0]])
	x2 = np.asarray([[0, 0, 0, 1], [0, 1, 1, 1], [1, 1, 0, 1]])
	"""
	training_set = [
		((0, 0, 0 ,1), 0),
		((1, 0, 1, 1), 0),
	    ((1, 0, 0, 1), 0),
	    ((1, 1, 0, 1), 0),
		((0, 0, 1, 1), 1),
	    ((0, 1, 1, 1), 1),
	    ((0, 1, 0, 1), 1),
	    ((1, 1, 1, 1), 1),
	]
	while True:
		error_count = 0
		for input_vector, desired_output in training_set:
			#print(weights)
			result = dot_product(input_vector, weights) > threshold
			error = desired_output - result
			if error != 0:
				error_count += 1
				for index, value in enumerate(input_vector):
					weights[index] += learning_rate * error * value
		if error_count == 0:
			break
	print weights

def perceptronAnd():
	threshold = 0.5
	learning_rate = 0.000001
	weights = [1, 1, 1]
	training_set = [
		((1, 0, 0), 0),
		((1, 0, 1), 0),
		((1, 1, 0), 0),
		((1, 1, 1), 1)
	]
	while True:
		#print('-' * 60)
		error_count = 0
		for input_vector, desired_output in training_set:
			#print(weights)
			result = dot_product(input_vector, weights) > threshold
			error = desired_output - result
			if error != 0:
				error_count += 1
				for index, value in enumerate(input_vector):
					weights[index] += learning_rate * error * value
		if error_count == 0:
			break

	plt3d = plt.figure().gca(projection='3d')
	plt3d.plot([0], [0], [0],c='r',marker='o')
	plt3d.plot([1], [0], [1],c='r',marker='o')
	plt3d.plot([1], [0], [0],c='r',marker='o')
	plt3d.plot([1], [1], [0],c='r',marker='o')
	plt3d.plot([0], [0], [1],c='r',marker='o')
	plt3d.plot([0], [1], [1],c='r',marker='o')
	plt3d.plot([0], [1], [0],c='r',marker='o')
	plt3d.plot([1], [1], [1],c='r',marker='o')
	#plt3d.plot_surface(xx,yy,z2, color='yellow')
	#plt3d.plot_surface(xx,yy,z3, color='cyan')
	plt.show()
#perceptronPractica()
perceptronAnd()
#perceptronWIKI()
#perceptronOR()