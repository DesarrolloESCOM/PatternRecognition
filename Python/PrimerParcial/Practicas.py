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
		print ">>>>>>>>>>>>>", distanciaMahalanobisArreglo
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
		for media in mediasClases:
			print "Medias \n", media
			print "\n ----------------------------------- \n"
		for i in range(0, len(clases)):
			mediasClasesTranspuestas.append(np.transpose(mediasClases[i]))
		for mediaTranspuesta in mediasClasesTranspuestas:
			print "Medias Transpuestas \n", mediaTranspuesta
			print "\n ----------------------------------- \n"
		for i in range(0, len(clases)):
			aux = []
			for j in range(0, len(clases[0][0])):
				aux.append((np.subtract(((clases[i])[:, j]), mediasClasesTranspuestas[i])))
			restaMediasClases.append(aux)
		for restaMediaClase in restaMediasClases:
			print "Resta Medias Clases \n", restaMediaClase
			print "\n ----------------------------------- \n"
		for matriz in restaMediasClases:
			aux = np.multiply((1.0 / len(clases[0][0])), np.dot(np.transpose(matriz), matriz))
			covarianzas.append(aux)
		indices = []
		for covarianza in covarianzas:
			print "Covarianzas \n", covarianza
			print "\n ----------------------------------- \n"
		for x in range(0, len(covarianzas) - 1):
			try:
				inversas.append(np.matrix(covarianzas[x]).I)
			except np.linalg.linalg.LinAlgError:
				print "Matriz no tiene inversa!!!"
				#se quita la clase que no cumple con la inversa
				indices.append(x)
			return distanciaMahalanobis(clases, vector, mediasClasesTranspuestas, inversas)


def CriterioKNN(clases, vector):
	distancias = []
	for i in range(0, len(clases)):
		for x in range(0, len((clases[0])[0])):
			#print (clases[i])[0][x]
			#print (clases[i])[1][x]
			#print (clases[i])[2][x]
			distancia = euclidean([(clases[i])[0][x], (clases[i])[1][x], (clases[i])[2][x]], vector)
			distancias.append([distancia , ('C'+str(i+1))])
	return sorted(distancias)

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
	maximoBayes = np.amax(probabilidadPorcentaje)
	claseBayes = probabilidadPorcentaje.index(maximoBayes)
	print  "El vector pertenece a la clase %s con un %s porcentaje utilizando el criterio de Bayes" % (
	(claseBayes + 1), maximoBayes)
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	plt.show()


def practica2():
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	clase1 = np.asarray([[1, 3, 1, 2, 3], [2, 5, 5, 2, 3]])
	clase2 = np.asarray([[6, 6, 7, 8, 8], [4, 3, 4, 4, 5]])
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
	maximoBayes = np.amax(probabilidadPorcentaje)
	claseBayes = probabilidadPorcentaje.index(maximoBayes)
	print "El vector pertenece a la clase %s con un porcentaje %s utilizando el criterio de Bayes" % (
	(claseBayes + 1), maximoBayes)
	print "---------------------------------------------------------------------------------------"
	criterioMahalanobis = distanciaMahalanobis(arregloClases, vectorUsuario)
	minimoMahalanobis = np.amin(criterioMahalanobis)
	claseMahalanobis = criterioMahalanobis.index(minimoMahalanobis)
	print "El vector pertenece a la clase %s con una distancia de %s  utilizando el criterio de Mahalanobis" % (
	(claseMahalanobis + 1), minimoMahalanobis)
	print "---------------------------------------------------------------------------------------"
	criterioEuclidiano = distanciaEuclidiana(arregloClases, vectorUsuario)
	minimoEuclidiano = np.amin(criterioEuclidiano)
	claseEuclidiano = criterioEuclidiano.index(minimoEuclidiano)
	print "El vector pertenece a la clase %s con una distancia de %s utilizando el criterio de la distancia euclidiana" % (
	(claseEuclidiano + 1), minimoEuclidiano)
	print "---------------------------------------------------------------------------------------"
	for x in range(0, 4):
		ax.scatter(clase1[:, x][0], clase1[:, x][1], c='r', marker='o')
	for x in range(0, 4):
		ax.scatter(clase2[:, x][0], clase2[:, x][1], c='b', marker='x')
	ax.scatter(vectorUsuario[0], vectorUsuario[1], c='y', marker='s')

	plt.show()


def practica3():
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	#ax.legend(loc=0, scatterpoints=1)
	sol = np.asarray([[757, 695, 672, 704, 771, 854, 837], [327, 345, 413, 483, 517, 447, 354]])
	#print np.shape(sol)
	tierra = np.asarray([[8, 231, 562, 1167, 1680, 2046, 2468], [201, 308, 389, 450, 414, 348, 206]])
	#print np.shape(tierra)
	espacio = np.asarray([[43, 298, 643, 1065, 1471, 1858, 2274], [414, 516, 618, 653, 648, 562, 470]])
	#print np.shape(espacio)
	#clase1 = np.asarray([[1, 3, 1, 2, 3], [2, 5, 5, 2, 3]])
	#clase2 = np.asarray([[6, 6, 7, 8, 8], [4, 3, 4, 4, 5]])
	vectorPrueba = np.asarray([[4], [5]])
	maximo = max(max([np.amax(sol), np.amax(tierra)]), np.amax(espacio)) + 1
	print("Introduce el vector a probar, cada coordenada debe encontrarse entre 0 y %s \n" % (maximo))
	vectorUsuario = []

	for x in range(0, 2):
		aux = float(raw_input())
		while aux > maximo:
			print ("El elemento debe estar entre los valores de 0 y %s" % (maximo))
			aux = float(raw_input())
		vectorUsuario.append(aux)
	vectorUsuario = np.asarray(vectorUsuario)
	arregloClases = [sol, tierra, espacio]
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
	##se imprime en consola los valores de la desicion
	maximoBayes = np.amax(probabilidadPorcentaje)
	claseBayes = probabilidadPorcentaje.index(maximoBayes)
	print "El vector pertenece a la clase %s con un porcentaje %s   utilizando el criterio de Bayes" % (
	(claseBayes + 1), maximoBayes)
	print "---------------------------------------------------------------------------------------"

	print "---------------------------------------------------------------------------------------"
	criterioEuclidiano = distanciaEuclidiana(arregloClases, vectorUsuario)
	minimoEuclidiano = np.amin(criterioEuclidiano)
	claseEuclidiano = criterioEuclidiano.index(minimoEuclidiano)
	print "El vector pertenece a la clase %s con una distancia de %s  utilizando el criterio de la distancia euclidiana" % (
	(claseEuclidiano + 1), minimoEuclidiano)
	print "---------------------------------------------------------------------------------------"
	scatterArray1 = []
	a = []
	print "Scatter Array", scatterArray1
	for x in range(0, 7):
		a.append([sol[:, x][0], sol[:, x][1]])
	ploteo1, = plt.plot(*zip(*a),marker='o', color='r',ls='')
	a = []
	for x in range(0, 7):
		a.append([tierra[:, x][0], tierra[:, x][1]])
	ploteo2, = plt.plot(*zip(*a), c='g', marker='x',ls='')
	a = []
	for x in range(0, 7):
		a.append([espacio[:, x][0], espacio[:, x][1]])
	ploteo3, = plt.plot(*zip(*a), c='b', marker='^',ls='')
	plt.legend([ploteo1,ploteo2,ploteo3], ['sol','tierra','espacio'])

	plt.title("Practica 3")
	plt.show()


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
	plt.imshow(imagenTresColores)
	plt.show()


def ejercicioCuatroExamenParcial1():
	jpegImage = Image.open("/home/alberto/Pictures/peppers2.png")
	imagenOriginal = np.asarray(jpegImage).copy()
	#plt.imshow(imagenOriginal)
	#clases = [[]] * 3
	x1 = np.asarray([[0, 1, 1, 1], [0, 0, 0, 1], [0, 1, 0, 0]])
	print np.shape(x1)
	clases1 = [[], [], []]
	clases2 = [[], [], []]
	clases3 = [[], [], []]
	#print clases
	print np.shape(clases1)
	#vectoresCaracteristicos = []
	#caracteristicosX = []
	caracteristicosY = []
	print imagenOriginal[120, 200]
	for x in range(120, 123):
		for y in range(0, 3):
			clases1[0].append(imagenOriginal[x, y, 0])
			clases1[1].append(0)
			clases1[2].append(0)
			#
			clases2[0].append(0)
			clases2[1].append(imagenOriginal[x, y, 1])
			clases2[2].append(0)
			#
			clases3[0].append(0)
			clases3[1].append(0)
			clases3[2].append(imagenOriginal[x, y, 2])
	vectorADeterminar = imagenOriginal[190, 466]
	print "Clase 1", clases1
	print "Clase 2", clases2
	print "Clase 3", clases3
	criterioMahalanobis = distanciaMahalanobis(np.asarray([clases1, clases2, clases3]), vectorADeterminar)


"""

	minimoMahalanobis = np.amin(criterioMahalanobis)
	claseMahalanobis = criterioMahalanobis.index(minimoMahalanobis)
	print "El vector pertenece a la clase %s con una distancia de %s  utilizando el criterio de Mahalanobis" % (
	(claseMahalanobis + 1), minimoMahalanobis)
	plt.show()"""


def ejercicioDosExamenParcial1():
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	clase1 = np.asarray([[0, 3, 2, 1, 5], [0, 8, 2, 1, 3]])
	clase2 = np.asarray([[4, 6, 5, 6, 7], [8, 3, 4, 4, 5]])
	maximo = max([np.amax(clase1), np.amax(clase2)]) + 1
	#print("Introduce el vector a probar, cada coordenada debe encontrarse entre 0 y %s \n" % (maximo))
	vectorUsuario = [-4.5, 3.9]

	#for x in range(0, 2):
	#		aux = float(raw_input())
	#while aux > maximo:
	#		print ("El elemento debe estar entre los valores de 0 y %s" % (maximo))
	#			aux = float(raw_input())#
	#vectorUsuario.append(aux)
	vectorUsuario = np.asarray(vectorUsuario)
	arregloClases = [clase1, clase2]
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
	print "PROBABILIDADES", probabilidadPorcentaje
	maximoBayes = np.amax(probabilidadPorcentaje)
	claseBayes = probabilidadPorcentaje.index(maximoBayes)
	print "El vector pertenece a la clase %s con un porcentaje %s utilizando el criterio de Bayes" % (
	(claseBayes + 1), maximoBayes)
	"""
	print "---------------------------------------------------------------------------------------"
	criterioMahalanobis = distanciaMahalanobis(arregloClases, vectorUsuario)
	minimoMahalanobis = np.amin(criterioMahalanobis)
	claseMahalanobis = criterioMahalanobis.index(minimoMahalanobis)
	print "El vector pertenece a la clase %s con una distancia de %s  utilizando el criterio de Mahalanobis" % (
	(claseMahalanobis + 1), minimoMahalanobis)
	print "---------------------------------------------------------------------------------------"
	criterioEuclidiano = distanciaEuclidiana(arregloClases, vectorUsuario)
	minimoEuclidiano = np.amin(criterioEuclidiano)
	claseEuclidiano = criterioEuclidiano.index(minimoEuclidiano)
	print "El vector pertenece a la clase %s con una distancia de %s utilizando el criterio de la distancia euclidiana" % (
	(claseEuclidiano + 1), minimoEuclidiano)
	print "---------------------------------------------------------------------------------------"
	"""
	scatterArray1 = []
	for x in range(0, 4):
		scatterArray1.append(ax.scatter(clase1[:, x][0], clase1[:, x][1], c='r', marker='o'))
	for x in scatterArray1:
		plt.legend([x], ['Clase1'], numpoints=1, loc=1)
	scatterArray2 = []
	for x in range(0, 4):
		scatterArray2.append(ax.scatter(clase2[:, x][0], clase2[:, x][1], c='b', marker='x'))
	for x in scatterArray2:
		plt.legend([x], ['Clase2'], numpoints=1, loc=1)

	scatterArray3 = []
	scatterArray3.append(ax.scatter(vectorUsuario[0], vectorUsuario[1], c='y', marker='s'))
	plt.legend(scatterArray3, ['Vector'], numpoints=1, loc=1)
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	plt.show()


#ejercicioCuatroExamenParcial1()

def PracticaKNN():
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	#se declaran las clases
	Clase1 = np.asarray([[200, 210, 215, 210, 198], [160, 170, 172, 165, 177], [120, 130, 133, 134, 138]])
	Clase2 = np.asarray([[90, 92, 87, 91, 55], [130, 138, 128, 164, 123], [60, 54, 66, 60, 55]])
	Clase3 = np.asarray([[30, 20, 24, 28, 22], [44, 40, 42, 50, 46], [178, 180, 184, 176, 181]])
	#se declaran los vectores del usuario
	vectorA = [[208], [170], [135]]
	vectorB = [[208], [40], [30]]
	#print Clase1[0,1]
	#print Clase1[1,1]
	#print Clase1[2,1]
	arregloClases = [Clase1, Clase2, Clase3]
	vecinosVectorA = CriterioKNN(arregloClases, vectorA)
	vecinosVectorB = CriterioKNN(arregloClases, vectorB)
	for elementoOrdenado in vecinosVectorA:
		print "\n"
		print elementoOrdenado
	print "\n-------------------------------------------\n"
	for elementoOrdenado in vecinosVectorB:
		print "\n"
		print elementoOrdenado
	#print "\n---------------------------------------------\n"
	#print vecinosVectorB
	#valorProbabilidad1 = distanciaBayesiana(arregloClases, vectorA)
	#valorProbabilidad2 = distanciaBayesiana(arregloClases, vectorB)
	for x in range(0, 5):
		ax.scatter(Clase1[:, x][0], Clase1[:, x][1], Clase1[:, x][2], c='r', marker='o')
	for x in range(0, 5):
		ax.scatter(Clase2[:, x][0], Clase2[:, x][1], Clase2[:, x][2], c='b', marker='x')
	for x in range(0, 5):
		ax.scatter(Clase3[:, x][0], Clase3[:, x][1], Clase3[:, x][2], c='b', marker='x')
	ax.scatter(vectorA[0], vectorA[1], vectorA[2], c='g', marker='s')
	ax.scatter(vectorB[0], vectorB[1], vectorB[2], c='w', marker='s')
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	plt.title("Practica KNN")
	plt.show()


#PracticaKNN()
practica3()