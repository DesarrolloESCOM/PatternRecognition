__author__ = 'alberto'
#Para poder mostrar en pantalla el proceso
debug = False
from math import sqrt
import cmath as Math
#from mpl_toolkits.mplot3d import axes3d, Axes3D
from mpl_toolkits.mplot3d import axes3d, Axes3D
import Image
from scipy.spatial.distance import euclidean
import numpy as np
import matplotlib.pyplot as plt

def distanciaBayesiana(clases, vector):
	#proceso de distancia bayesiana
	#para obtener las medias
	mediasClases = []
	mediasClasesTranspuestas = []
	restaMediasClases = []
	covarianzas = []
	inversas = []
	probabilidades = []
	for i in range(0, len(clases)):
		mediasClases.append(clases[i].mean(1))
	for i in range(0, len(clases)):
		mediasClasesTranspuestas.append(np.transpose(mediasClases[i]))
	for i in range(0, len(clases)):
		aux = []
		for j in range(0, len(clases[0][0])):
			aux.append((np.subtract(((clases[i])[:, j]), mediasClasesTranspuestas[i])))
		restaMediasClases.append(aux)
	for matriz in restaMediasClases:
		aux = np.multiply((1.0 / len(clases[0][0])), np.dot(np.transpose(matriz), matriz))
		covarianzas.append(aux)

	for elemento in covarianzas:
		inversas.append(np.matrix(elemento).I)
	for i in range(0, len(clases)):
		parte1 = float((1.0 / (pow(Math.pi, ((len(clases) / 2.0)))) * (sqrt(abs(np.linalg.det(covarianzas[i]))))))
		distanciaMahalanobisValor = distanciaMahalanobis(clases, vector, mediasClasesTranspuestas, inversas)
		parte2 = pow(Math.e, ((-1.0 / 2) * distanciaMahalanobisValor[i]))
		probabilidades.append(float(parte1 * parte2))
	if debug:
		print "MATRICES COVARIANZA \n"
		print covarianzas
		print "MATRICES MEDIA\n"
		print mediasClases
		print "MATRICES INVERSAS\n"
		print inversas
	return probabilidades

def distanciaBayesianaEtiquetas(clases, vector):
	#proceso de distancia bayesiana
	#para obtener las medias
	mediasClases = []
	mediasClasesTranspuestas = []
	restaMediasClases = []
	covarianzas = []
	inversas = []
	probabilidades = []
	for i in range(0, len(clases)):
		mediasClases.append(clases[i].mean(1))
	for i in range(0, len(clases)):
		mediasClasesTranspuestas.append(np.transpose(mediasClases[i]))
	for i in range(0, len(clases)):
		aux = []
		for j in range(0, len(clases[0][0])):
			aux.append((np.subtract(((clases[i])[:, j]), mediasClasesTranspuestas[i])))
		restaMediasClases.append(aux)
	for matriz in restaMediasClases:
		aux = np.multiply((1.0 / len(clases[0][0])), np.dot(np.transpose(matriz), matriz))
		covarianzas.append(aux)

	for elemento in covarianzas:
		inversas.append(np.matrix(elemento).I)
	for i in range(0, len(clases)):
		parte1 = float((1.0 / (pow(Math.pi, ((len(clases) / 2.0)))) * (sqrt(abs(np.linalg.det(covarianzas[i]))))))
		distanciaMahalanobisValor = distanciaMahalanobis(clases, vector, mediasClasesTranspuestas, inversas)
		parte2 = pow(Math.e, ((-1.0 / 2) * distanciaMahalanobisValor[i]))
		probabilidades.append([float(parte1 * parte2),(str(i+1))])
	probabilidades = sorted(probabilidades)
	return [probabilidades[-1]]

def distanciaEuclidiana(clases, vector, medias=[]):
	distancias = []
	if len(medias) > 0:  #ya no se procesan las medias
		for i in range(0, len(clases)):
			distancia = euclidean(medias[i], vector)
			distancias.append(distancia)
	else:
		mediasClases = []
		for i in range(0, len(clases)):
			mediasClases.append(clases[i].mean(1))
		for i in range(0, len(clases)):
			distancia = euclidean(mediasClases[i], vector)
			distancias.append(distancia)
	return distancias
def distanciaMahalanobis(clases, vector, medias=[], covarianzasInversas=[]):
	restaVectores = []
	restaVectoresTranspuesta = []
	distanciaMahalanobisArreglo = []
	if (len(medias) > 0) and (len(covarianzasInversas) > 0):  #existen las medias y las covarianzas
		for i in range(0, len(medias)):
			restaVectores.append(np.subtract(vector, medias[i]))
		for i in range(0, len(medias)):
			restaVectoresTranspuesta.append(np.transpose(restaVectores[i]))
		for i in range(0, len(medias)):
			aux = np.dot(np.dot(restaVectoresTranspuesta[i], covarianzasInversas[i]), restaVectores[i])
			distanciaMahalanobisArreglo.append(aux.item((0, 0)))
		#print ">>>>>>>>>>>>>", distanciaMahalanobisArreglo
		return distanciaMahalanobisArreglo
	else:
		#se realiza todo el proceso de calculo de las varianzas y matrices inversas
		mediasClases = []
		mediasClasesTranspuestas = []
		restaMediasClases = []
		covarianzas = []
		inversas = []
		for i in range(0, len(clases)):
			mediasClases.append(clases[i].mean(1))
		for i in range(0, len(clases)):
			mediasClasesTranspuestas.append(np.transpose(mediasClases[i]))
		for i in range(0, len(clases)):
			aux = []
			for j in range(0, len(clases[0][0])):
				aux.append((np.subtract(((clases[i])[:, j]), mediasClasesTranspuestas[i])))
			restaMediasClases.append(aux)
		for matriz in restaMediasClases:
			aux = np.multiply((1.0 / len(clases[0][0])), np.dot(np.transpose(matriz), matriz))
			covarianzas.append(aux)
		indices = []
		for x in range(0, len(covarianzas) - 1):
			try:
				inversas.append(np.matrix(covarianzas[x]).I)
			except np.linalg.linalg.LinAlgError:
				print "Matriz no tiene inversa!!!"
				#se quita la clase que no cumple con la inversa
				indices.append(x)
		return distanciaMahalanobis(clases, vector, mediasClasesTranspuestas, inversas)

def CriterioKNN(clases, vector, cantidad = 1):
	distancias = []
	for i in range(0, len(clases)):
		for x in range(0, len((clases[0])[0])):
			aux = []
			for j in xrange(0,len((clases[0]))):
				aux.append((clases[i])[j][x])
			distancia = euclidean(aux, vector)
			distancias.append([distancia , (str(i+1))])
	#print distancias
	distanciasAcomodadas = sorted(distancias)
	arregloFinal = []
	for i in xrange(0,cantidad):
		arregloFinal.append(distanciasAcomodadas[i])
	#print "-"*70+"\n"
	#print arregloFinal
	#print "-"*70+"\n"
	return arregloFinal