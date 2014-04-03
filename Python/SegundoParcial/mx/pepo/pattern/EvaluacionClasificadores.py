__author__ = 'alberto'

from Distancias import *
import random

def CrossValidation(clases=[]):
	tablaEvaluacion = np.zeros((len(clases) + 1, len(clases) + 1), dtype=np.float)
	general = []
	for i in range(0, len(clases)):
		for x in range(0, len((clases[0])[0])):
			aux = []
			for j in xrange(0,len(clases[0])):
				aux.append((clases[i])[0][x])
			general.append(aux)

	random.shuffle(general)

	for i in range(0,len(general)/2):
		general.pop()
	for i in range(0, len(clases)):
		for x in range(i*len((clases[0])[0]),(i+1)*len((clases[0])[0])):
			if x >= len(general):
				break
			else:
				resultado = CriterioKNN(clases, general[x])
				tablaEvaluacion[i][int(resultado[1]) - 1] += 1
	for i in range(0, len(clases)):
		tablaEvaluacion[-1, -1] += tablaEvaluacion[i, i]
	tablaEvaluacion[-1, -1] = tablaEvaluacion[-1, -1] / len(general) * 100
	#print tablaEvaluacion
	return tablaEvaluacion

def leaveOneOut(clases):  #No recuerdo el nombre
	tablaEvaluacion = np.zeros((len(clases) + 1, len(clases) + 1), dtype=np.float)
	general = []
	for i in range(0, len(clases)):
		for x in range(0, len((clases[0])[0])):
			aux = []
			for j in xrange(0,len((clases[0]))):
				aux.append((clases[i])[j][x])
			general.append(aux)
	general.pop()
	random.shuffle(general)
	for i in range(0, len(clases)):
		for x in range(i*len((clases[0])[0]),(i+1)*len((clases[0])[0])):
			if x >= len(general):
				break
			else:
				resultado = CriterioKNN(clases, general[x])
				tablaEvaluacion[i][int(resultado[1]) - 1] += 1
	for i in range(0, len(clases)):
		tablaEvaluacion[-1, -1] += tablaEvaluacion[i, i]
	tablaEvaluacion[-1, -1] = tablaEvaluacion[-1, -1] / len(general) * 100
	#print tablaEvaluacion
	return tablaEvaluacion

def resampling(clases):  #
	tablaEvaluacion = np.zeros((len(clases) + 1, len(clases) + 1), dtype=np.float)
	contadorElementos = 0
	for i in range(0, len(clases)):
		for x in range(0, len((clases[0])[0])):
			aux = []
			for x in xrange(0,len(clases[0])):
				aux.append((clases[i])[0][x])
			resultado = CriterioKNN(clases, aux)
			tablaEvaluacion[i][int(resultado[1]) - 1] += 1
			contadorElementos += 1
	for i in range(0, len(clases)):
		tablaEvaluacion[-1, -1] += tablaEvaluacion[i, i]
	tablaEvaluacion[-1, -1] = tablaEvaluacion[-1, -1] / contadorElementos * 100
	return tablaEvaluacion