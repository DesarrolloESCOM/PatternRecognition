import numpy as np

MatrizA = np.array([-0.25,0.25,-0.25])
MatrizB = np.array([[8,-4,-4],[-4,8,4],[-4,4,8]])
ResultadoMatrices = np.dot(np.dot(MatrizA,MatrizB),np.transpose(MatrizA))
print ResultadoMatrices
