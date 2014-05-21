#from mpl_toolkits.mplot3d import axes3d, Axes3D
from mpl_toolkits.mplot3d import axes3d, Axes3D
from EvaluacionClasificadores import resampling,leaveOneOut,CrossValidation
import numpy as np
import matplotlib.pyplot as plt
from Distancias import CriterioKNN
def PracticaKNN():
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	#se declaran las clases
	Clase1 = np.asarray([[200, 210, 215, 210, 198], [160, 170, 172, 165, 177], [120, 130, 133, 134, 138]])
	Clase2 = np.asarray([[90, 92, 87, 91, 55], [130, 138, 128, 164, 123], [60, 54, 66, 60, 55]])
	Clase3 = np.asarray([[30, 20, 24, 28, 22], [44, 40, 42, 50, 46], [178, 180, 184, 176, 181]])

	#se declaran los vectores del usuario
	vectorA = [[208], [170], [135]]
	vectorB = [[0], [40], [30]]

	arregloClases = [Clase1, Clase2, Clase3]
	#print np.shape(arregloClases)
	#vecinosVectorA = CriterioKNN(arregloClases, vectorA)
	#vecinosVectorB = CriterioKNN(arregloClases, vectorB)
	print "\n----------------RESUSTITUCION---------------------------\n"
	resustitucion = resampling(arregloClases)
	print resustitucion
	print "\n----------------LEAVE ONE OUT---------------------------\n"
	quitaUno = leaveOneOut(arregloClases)
	print quitaUno
	print "\n----------------CRUZADO ---------------------------\n"
	cruzado = CrossValidation(arregloClases)
	print cruzado
	print "\n-------------------------------------------\n"
	#print vecinosVectorA
	#print "\n-------------------------------------------\n"
	#print vecinosVectorB
	#print "\n---------------------------------------------\n"
	for x in range(0, 5):
		ax.scatter(Clase1[:, x][0], Clase1[:, x][1], Clase1[:, x][2], c='r', marker='o')
	for x in range(0, 5):
		ax.scatter(Clase2[:, x][0], Clase2[:, x][1], Clase2[:, x][2], c='b', marker='x')
	for x in range(0, 5):
		ax.scatter(Clase3[:, x][0], Clase3[:, x][1], Clase3[:, x][2], c='b', marker='^')
	#ax.scatter(vectorA[0], vectorA[1], vectorA[2], c='g', marker='s')
	#ax.scatter(vectorB[0], vectorB[1], vectorB[2], c='w', marker='s')
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	plt.title("Practica KNN")
	plt.show()
PracticaKNN()