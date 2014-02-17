__author__ = 'alberto'
from django.http import HttpResponse
from scipy import misc

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


def index(response):
	image = misc.imread("/home/alberto/Downloads/WP_001922.jpg")
	#contenido = image.shape
	contenido2 = image.dtype
	return HttpResponse(contenido2)


def matrixOperations(response):
	contenido = "Operacion con Matrices"
	return HttpResponse(contenido)