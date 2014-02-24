__author__ = 'alberto'
from django.http import HttpResponse
#import Image
from django.shortcuts import render


'''

import Image
import matplotlib.pyplot as plt
from scipy import misc
jpegImage = Image.open("/home/alberto/Downloads/WP_001922.jpg")
print jpegImage.bits, jpegImage.size, jpegImage.format
print "\nok"
print "---------------------------------------\n"
l = misc.lena()
image = misc.imread("/home/alberto/Downloads/WP_001922.jpg")
plt.imshow(image)
plt.show()
print "\n"
print type(image)
print "\n"
print image.shape, image.dtype
'''

#Para cargar la pagina inicial
def index(request):
	return render(request, 'index.html')

#Para regresar el contenido del cubo
def cubo(request):
	contenido = "cubo"
	return HttpResponse(contenido)

#para cargar la vista de las clases
def clases(request):
	contenido = "clases"
	return HttpResponse(contenido)

#para cargar la vista de las imagenes
def imagen(request):
	contenido = "imagen"
	return HttpResponse(contenido)
#para cargar la vista con las banderas ya procesadas
def banderas(request):
	contenido = "Banderas"
	return HttpResponse(contenido)