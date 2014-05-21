__author__ = 'alberto'
from Distancias import *
from EvaluacionClasificadores import *
import matplotlib.pyplot as plt
import random
import numpy as np
def ejercicio1():
	im = plt.imread("/home/alberto/Pictures/peppers2.png")
	implot = plt.imshow(im)
	# put a blue dot at (10, 20)
	plt.scatter([10], [20])
	# put a red dot, size 40, at 2 locations:
	plt.scatter(x=[30, 40], y=[50, 60], c='r', s=40)
	plt.show()
def ejercicio1Examen():
	centroides = []
	clases = []
	Noclases = 4
	VecinosPorClase = 30
	vecinosAConsiderar = 3
	dispercionVecinos = [20,40,20,60]
	#Centroides por clase
	centroides.append([268 , 212])
	centroides.append([274 , 286])
	centroides.append([416 , 208])
	centroides.append([468 , 284])
	for i in xrange(0, Noclases):
		coordenadasX = []
		coordenadasY = []
		for j in xrange(0, VecinosPorClase - 1):
			#se generan los aleatorios
			coordenadasX.append(random.uniform(centroides[i][0], (centroides[i][0] + dispercionVecinos[i])))
			coordenadasY.append(random.uniform(centroides[i][1], (centroides[i][1] + dispercionVecinos[i])))
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
	fig = plt.imread("/home/alberto/Pictures/peppers2.png")
	implot = plt.imshow(fig)
	#ax = fig.add_subplot(1, 1, 1)
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
	#ax.set_xlabel('X')
	#ax.set_ylabel('Y')
	plt.show()
def ejercicio2Examen():
	centroides = []
	clases = []
	Noclases = 4
	VecinosPorClase = 500
	vecinosAConsiderar = 3
	dispercionVecinos = [20,40,20,60]
	vectorAClasificar = [345,247]
	#Centroides por clase
	centroides.append([268 , 212])
	centroides.append([274 , 286])
	centroides.append([416 , 208])
	centroides.append([468 , 284])
	for i in xrange(0, Noclases):
		coordenadasX = []
		coordenadasY = []
		for j in xrange(0, VecinosPorClase - 1):
			#se generan los aleatorios
			coordenadasX.append(random.uniform(centroides[i][0], (centroides[i][0] + dispercionVecinos[i])))
			coordenadasY.append(random.uniform(centroides[i][1], (centroides[i][1] + dispercionVecinos[i])))
		coordenadasX.append(centroides[i][0])
		coordenadasY.append(centroides[i][1])
		clases.append([coordenadasX, coordenadasY])
	clases = np.asarray(clases)
	vectorAClasificar = np.asarray(vectorAClasificar)
	#
	# Evaluacion de las distancias respectoa  cada clase
	#
	probabilidades = distanciaBayesiana(clases,vectorAClasificar)
	probabilidadesConEtiqueta = []
	sumaTotal = 0.0
	probabilidadPorcentaje = []
	for elemento in probabilidades:
		sumaTotal += elemento
	for i in range(0, len(probabilidades)):
		aux = (probabilidades[i] / sumaTotal) * 100
		probabilidadPorcentaje.append(aux)
	for i in range(0,len(clases)):
		probabilidadesConEtiqueta.append([probabilidadPorcentaje[i],"C"+(str(i+1))])
	probabilidadesConEtiqueta = sorted(probabilidadesConEtiqueta)
	for elemento in probabilidadesConEtiqueta:
		print "El vector pertenece a la clase %s con %s de probabilidad"%(elemento[1],elemento[0])
	final = probabilidadesConEtiqueta[-1]
	print "El vector dado pertenece a la clase %s con %s de probabilidad " % (final[1],final[0])
	#
	# Evaluacion de los clasificadores
	#
	print "-"*60+" Leave one out "+"-"*60+"\n"
	#quitaUno = leaveOneOut(clases)
	#print quitaUno
	print "-"*60+" Cross Validation "+"-"*60+"\n"
	#crossValidation = CrossValidation(clases)
	#print crossValidation
	print "-"*60+" Resampling "+"-"*60+"\n"
	pruebaTodos = resampling(clases)
	print pruebaTodos
	print "-"*60+"\n"
	#
	# Generacion de la grafica
	#
	fig = plt.imread("/home/alberto/Pictures/peppers2.png")
	implot = plt.imshow(fig)
	#ax = fig.add_subplot(1, 1, 1)
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
	plt.plot(*zip(vectorAClasificar),c='blue',marker='D',ls='')
	plt.legend(leyendasClases, loc=4, numpoints=4)
	plt.title("Practica 2")
	#ax.set_xlabel('X')
	#ax.set_ylabel('Y')
	plt.show()
#ejercicio1Examen()
ejercicio2Examen()