__author__ = 'alberto'
from math import sqrt
import cmath as Math
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
		#distanciaMahalanobisValor = distanciaMahalanobis(clases, vector)
		parte2 = pow(Math.e, ((-1.0 / 2) * distanciaMahalanobisValor[i]))
		probabilidades.append(float(parte1 * parte2))
	#print probabilidades
	return probabilidades


def distanciaEuclidiana(clases, vector, medias=[]):
	distancias = []
	if len(medias) > 0:  #ya no se procesan las medias
		for i in range(0, len(clases)):
			distancia = np.linalg.norm((medias[i] - vector))
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
		#print distanciaMahalanobisArreglo
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

		for elemento in covarianzas:
			inversas.append(np.matrix(elemento).I)
		return distanciaMahalanobis(clases, vector, mediasClasesTranspuestas, inversas)


def practica1():
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	x1 = np.asarray([[0, 1, 1, 1], [0, 0, 0, 1], [0, 1, 0, 0]])
	x2 = np.asarray([[0, 0, 0, 1], [0, 1, 1, 1], [1, 1, 0, 1]])
	#se cargan los datos de la primer clase
	for x in range(0, 4):
		ax.scatter(x1[:, x][0], x1[:, x][1], x1[:, x][2], c='r', marker='o')
	#se cargan los datos de la segunda clase
	for x in range(0, 4):
		ax.scatter(x2[:, x][0], x2[:, x][1], x2[:, x][2], c='b', marker='x')
	'''
	Se realizan las operaciones necesarias para saber a que clase pertenece
	'''
	print("Introduce el vector a probar, cada coordenada debe encontrarse entre 0 y 1.5 \n")
	vectorUsuario = []
	for x in range(0, 3):
		aux = float(raw_input())
		while aux > 1.5:
			aux = float(raw_input("El elemento debe estar entre los valores de 0 y 1.5"))
		vectorUsuario.append(aux)
	vectorUsuario = np.asarray(vectorUsuario)
	#vectorUsuario = np.asarray([0.1, 0.5, 0.9])
	#se aniade el vector que introduzca el usuario
	ax.scatter(vectorUsuario[0], vectorUsuario[1], vectorUsuario[2], c='y', marker='s')
	arregloClases = [x1, x2]
	#se calcula la distancia usando la distancia Bayesiana
	valorProbabilidad = distanciaBayesiana(arregloClases, vectorUsuario)
	#valorProbabilidad = distanciaBayesiana(arregloClases, vectorUsuario)
	print valorProbabilidad
	sumaTotal = 0.0
	probabilidadPorcentaje = []
	for elemento in valorProbabilidad:
		sumaTotal += elemento
	for i in range(0, len(valorProbabilidad)):
		aux = (valorProbabilidad[i] / sumaTotal) * 100
		probabilidadPorcentaje.append(aux)
	print "Clase 1", probabilidadPorcentaje[0]
	print "Clase 2", probabilidadPorcentaje[1]
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	plt.show()


def practica2():
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	clase1 = np.asarray([[1, 3, 1, 2, 3], [2, 5, 5, 2, 3]])
	clase2 = np.asarray([[6, 6, 7, 8, 8], [4, 3, 4, 4, 5]])
	vectorPrueba = np.asarray([[4], [5]])
	maximo = max([np.amax(clase1), np.amax(clase2)]) + 1
	print("Introduce el vector a probar, cada coordenada debe encontrarse entre 0 y %s \n" % (maximo))
	vectorUsuario = []

	for x in range(0, 2):
		aux = float(raw_input())
		while aux > maximo:
			print ("El elemento debe estar entre los valores de 0 y %s" % (maximo))
			aux = float(raw_input())
		vectorUsuario.append(aux)
	vectorUsuario = np.asarray(vectorUsuario)
	arregloClases = [clase1, clase2]
	print distanciaBayesiana(arregloClases, vectorUsuario)
	print distanciaMahalanobis(arregloClases, vectorUsuario)
	print distanciaEuclidiana(arregloClases, vectorUsuario)
	for x in range(0, 4):
		ax.scatter(clase1[:, x][0], clase1[:, x][1], c='r', marker='o')
	for x in range(0, 4):
		ax.scatter(clase2[:, x][0], clase2[:, x][1], c='b', marker='x')
	ax.scatter(vectorUsuario[0], vectorUsuario[1], c='y', marker='s')
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	plt.show()


def practica3():
	pass


def practica4():
	jpegImage = Image.open("/home/alberto/Pictures/Webcam/pepo.jpg")
	imagenOriginal = np.asarray(jpegImage).copy()
	imagenRoja = np.asarray(jpegImage).copy()
	imagenVerde = np.asarray(jpegImage).copy()
	imagenAzul = np.asarray(jpegImage).copy()
	imagenTresColores = np.asarray(jpegImage).copy()
	imagenTresColoresVertical = np.asarray(jpegImage).copy()
	imagenCruz = np.asarray(jpegImage).copy()
	dimensiones = np.shape(imagenOriginal)
	imagenHorizontal = Image.new("RGB", (dimensiones[1] * 2, dimensiones[0] * 2))
	imagenVertical = Image.new("RGB", (dimensiones[1], dimensiones[0] * 4))
	#imagen roja
	imagenRoja[:, :, 1] = 0
	imagenRoja[:, :, 2] = 0
	#imagen verde
	imagenVerde[:, :, 0] = 0
	imagenVerde[:, :, 2] = 0
	#imagen azul
	imagenAzul[:, :, 0] = 0
	imagenAzul[:, :, 1] = 0
	#imagen horizontal
	imagenHorizontal.paste(Image.fromarray(imagenOriginal), (0, 0))
	imagenHorizontal.paste(Image.fromarray(imagenRoja), (dimensiones[1], 0))
	imagenHorizontal.paste(Image.fromarray(imagenVerde), (dimensiones[1], dimensiones[0]))
	imagenHorizontal.paste(Image.fromarray(imagenAzul), (0, dimensiones[0]))
	#imagen vertical
	imagenVertical.paste(Image.fromarray(imagenOriginal), (0, 0))
	imagenVertical.paste(Image.fromarray(imagenRoja), (0, dimensiones[0]))
	imagenVertical.paste(Image.fromarray(imagenVerde), (0, dimensiones[0] * 2))
	imagenVertical.paste(Image.fromarray(imagenAzul), (0, dimensiones[0] * 3))
	#imagen tres colores horizontal
	#imagen roja
	for x in range(0, (dimensiones[1] / 3)):
		imagenTresColores[:, x, 1] = 0
		imagenTresColores[:, x, 2] = 0
	#imagen verde
	for x in range((dimensiones[1] / 3), (2 * dimensiones[1] / 3)):
		imagenTresColores[:, x, 0] = 0
		imagenTresColores[:, x, 2] = 0
	#imagen azul
	for x in range((2 * dimensiones[1] / 3), dimensiones[1]):
		imagenTresColores[:, x, 0] = 0
		imagenTresColores[:, x, 1] = 0
	#
	#imagen tres colores vertical
	#imagen roja
	for x in range(0, (dimensiones[0] / 3)):
		imagenTresColoresVertical[x, :, 1] = 0
		imagenTresColoresVertical[x, :, 2] = 0
	#imagen verde
	for x in range((dimensiones[0] / 3), (2 * dimensiones[0] / 3)):
		imagenTresColoresVertical[x, :, 0] = 0
		imagenTresColoresVertical[x, :, 2] = 0
	#imagen azul
	for x in range((2 * dimensiones[0] / 3), dimensiones[0]):
		imagenTresColoresVertical[x, :, 0] = 0
		imagenTresColoresVertical[x, :, 1] = 0

	#
	#imagen con barrido cruz
	#
	#primer cuadro rojo
	for x in range(0, 100):
		for y in range(0, 100):
			imagenCruz[x, y, 1] = 0
			imagenCruz[x, y, 2] = 0
	#barrido verde lateral
	for x in range(0, 100):
		for y in range(100, (dimensiones[1] - 100)):
			imagenCruz[x, y, 0] = 0
			imagenCruz[x, y, 2] = 0
	#segundo cuadro en rojo
	for x in range(0, 100):
		for y in range((dimensiones[1] - 100), dimensiones[1]):
			imagenCruz[x, y, 1] = 0
			imagenCruz[x, y, 2] = 0
	#parte mas grande verde
	for x in range(100, (dimensiones[0] - 100)):
		imagenCruz[x, :, 0] = 0
		imagenCruz[x, :, 2] = 0
	#primer cuadro azul
	for x in range((dimensiones[0] - 100), dimensiones[0]):
		for y in range(0, 100):
			imagenCruz[x, y, 0] = 0
			imagenCruz[x, y, 1] = 0
	#parte verde
	for x in range((dimensiones[0] - 100), dimensiones[0]):
		for y in range(100, (dimensiones[1] - 100)):
			imagenCruz[x, y, 0] = 0
			imagenCruz[x, y, 2] = 0
	#segundo cuadro azul
	for x in range((dimensiones[0] - 100), dimensiones[0]):
		for y in range((dimensiones[1] - 100), (dimensiones[1])):
			imagenCruz[x, y, 0] = 0
			imagenCruz[x, y, 1] = 0
	plt.imshow(imagenCruz)
	plt.show()

	pass


print("Practicas Pattern Recognition \n")
print("1 Cubo \n")
print("2 Distancias \n")
print("3 Imagen \n")
print("4 Banderas \n")
opcion = int(raw_input("Selecciona una opcion:"))
if opcion is 1:
	practica1()
if opcion is 2:
	practica2()
if opcion is 3:
	practica3()
if opcion is 4:
	practica4()
