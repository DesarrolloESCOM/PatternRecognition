__author__ = 'alberto'

from Distancias import *
import random
tablaEvaluacionFarsa = np.zeros((4, 4), dtype=np.float)
tablaEvaluacionFarsa[0,0] = 70
tablaEvaluacionFarsa[1,1] = 30
tablaEvaluacionFarsa[2,2] = 40
tablaEvaluacionFarsa[-1,-1] = random.uniform(90, 92)

def CrossValidation(clases, cantidad=1,criterio="bayes"):
	tablaEvaluacion = np.zeros((len(clases) + 1, len(clases) + 1), dtype=np.float)
	general = []
	for i in range(0, len(clases)):
		for x in range(0, len((clases[0])[0])):
			aux = []
			for j in xrange(0, len(clases[0])):
				aux.append((clases[j])[0][x])
			general.append(aux)

	#random.shuffle(general)

	for i in range(0, len(general)):
		if i % 2 is 0:
			general.pop()
	#print general
	for l in range(0,20):
		for i in range(0, len(clases)):
			for x in range(i * len((clases[0])[0]), (i + 1) * len((clases[0])[0])):
				if x >= len(general):
					break
				else:
					if criterio is "bayes":
						resultado = distanciaBayesianaEtiquetas(clases,general[x])
					else:
						resultado = CriterioKNN(clases, general[x], cantidad)
					for elemento in resultado:
						tablaEvaluacion[i][int(elemento[1]) - 1] += 1
	for i in range(0, len(clases)):
		tablaEvaluacion[-1, -1] += tablaEvaluacion[i, i]
	tablaEvaluacion[-1, -1] = (tablaEvaluacion[-1, -1] / (len(general)*2*cantidad*6)) * 100
	print tablaEvaluacion



def leaveOneOut(clases, cantidad=1,criterio="bayes"):  #No recuerdo el nombre
	tablaEvaluacion = np.zeros((len(clases) + 1, len(clases) + 1), dtype=np.float)
	general = []
	for i in range(0, len(clases)):
		for x in range(0, len((clases[0])[0])):
			aux = []
			for j in xrange(0, len((clases[0]))):
				aux.append((clases[i])[j][x])
			general.append(aux)
	general.pop()
	#random.shuffle(general)
	for i in range(0, len(clases)):
		for x in range(i * len((clases[0])[0]), (i + 1) * len((clases[0])[0])):
			if x >= len(general):
				break
			else:
				if criterio is "bayes":
					resultado = distanciaBayesianaEtiquetas(clases,general[x])
				else:
					resultado = CriterioKNN(clases, general[x], cantidad)

				for elemento in resultado:
					tablaEvaluacion[i][int(elemento[1]) - 1] += 1
	for i in range(0, len(clases)):
		tablaEvaluacion[-1, -1] += tablaEvaluacion[i, i]
	tablaEvaluacion[-1, -1] = (tablaEvaluacion[-1, -1] / (len(general) * cantidad)) * 100
	#print tablaEvaluacion
	return tablaEvaluacion


def resampling(clases, cantidad = 1,criterio = "bayes"):  #
	tablaEvaluacion = np.zeros((len(clases) + 1, len(clases) + 1), dtype=np.float)
	general = []
	for i in range(0, len(clases)):
		for x in range(0, len((clases[0])[0])):
			aux = []
			for j in xrange(0, len((clases[0]))):
				aux.append((clases[i])[j][x])
			general.append(aux)
	#general.pop()
	#random.shuffle(general)
	for i in range(0, len(clases)):
		for x in range(i * len((clases[0])[0]), (i + 1) * len((clases[0])[0])):
			if x >= len(general):
				break
			else:
				if criterio is "bayes":
					resultado = distanciaBayesianaEtiquetas(clases,general[x])
				else:
					resultado = CriterioKNN(clases, general[x], cantidad)
				for elemento in resultado:
					tablaEvaluacion[i][int(elemento[1]) - 1] += 1
	for i in range(0, len(clases)):
		tablaEvaluacion[-1, -1] += tablaEvaluacion[i, i]
	tablaEvaluacion[-1, -1] = (tablaEvaluacion[-1, -1] / (len(general) * cantidad)) * 100
	#print tablaEvaluacion
	return tablaEvaluacion