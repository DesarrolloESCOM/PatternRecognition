__author__ = 'alberto'

from EvaluacionClasificadores import *

import random

import matplotlib.pyplot as plt
import numpy as np


def practicaGeneraClases():
	centroides = []
	clases = []
	print "Cuantas clases desea crear? Minimo 2 \n"
	Noclases = int(raw_input())
	print "Cuantos vecinos por clase? \n"
	VecinosPorClase = int(raw_input())
	print "Cuantos vecinos a considerar en al evaluacion? \n"
	vecinosAConsiderar = int(raw_input())
	print "Cuanta dispercion desde el centro de la clase ? \n"
	dispercionVecinos = int(raw_input())
	for i in xrange(0, Noclases):
		print "Anota el centro de la clase %s \n" % str(i + 1)
		entrada = raw_input()
		centroides.append([int(entrada.split()[0]), int(entrada.split()[1])])
	for i in xrange(0, Noclases):
		coordenadasX = []
		coordenadasY = []
		for j in xrange(0, VecinosPorClase - 1):
			#se generan los aleatorios
			coordenadasX.append(random.uniform(centroides[i][0], (centroides[i][0] + dispercionVecinos)))
			coordenadasY.append(random.uniform(centroides[i][1], (centroides[i][1] + dispercionVecinos)))
		coordenadasX.append(centroides[i][0])
		coordenadasY.append(centroides[i][1])
		clases.append([coordenadasX, coordenadasY])
	#
	# Evaluacion de los clasificadores
	#
	print "-"*60+" Leave one out "+"-"*60+"\n"
	quitaUno = leaveOneOut(clases,vecinosAConsiderar)
	print quitaUno
	print "-"*60+" Cross Validation "+"-"*60+"\n"
	crossValidation = CrossValidation(clases,vecinosAConsiderar)
	print crossValidation
	print "-"*60+" Resampling "+"-"*60+"\n"
	pruebaTodos = resampling(clases,vecinosAConsiderar)
	print pruebaTodos
	print "-"*60+"\n"
	#
	# Generacion de la grafica
	#
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	marcadores = ".,ov^<>12348sp*hH+xDd|_"
	ploteo = []
	for x in xrange(0, Noclases):
		ploteo.append([])
	leyendasClases = []
	contenido = []
	for x in xrange(0, Noclases):
		for j in xrange(0, VecinosPorClase):
			contenido.append([clases[x][0][j], clases[x][1][j]])
		ploteo[x], = plt.plot(*zip(*contenido), c=np.random.rand(3, 1),
		                      marker=marcadores[random.randrange(0, len(marcadores))], ls='')
		leyendasClases.append('C' + str(x + 1))
		contenido = []

	plt.legend(leyendasClases, loc=4, numpoints=4)
	plt.title("Practica 2")
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	plt.show()

practicaGeneraClases()