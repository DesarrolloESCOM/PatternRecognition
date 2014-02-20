__author__ = 'alberto'
from django.http import HttpResponse
from scipy import misc
#import Image
from django.template.loader import get_template
from django.template import Context
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


def index(request):
	image = misc.imread("/home/alberto/Downloads/WP_001922.jpg")
	#contenido = image.shape
	contenido2 = image.dtype
	return HttpResponse(contenido2)


def matrixOperations(request):
	contenido = "Operacion con Matrices"
	return HttpResponse(contenido)

def templateRender(request):
	template = get_template('test.html')
	htmlResponse = template.render(Context({'message':'Hola Mundo template'}))
	return HttpResponse(htmlResponse)
def shortCutRender(request):
	return render(request, 'test.html', {'mensaje': 'Prueba con shortcut como Grails'})
