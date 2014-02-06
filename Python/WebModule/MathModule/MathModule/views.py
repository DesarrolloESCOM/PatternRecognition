from django.http import HttpResponse 
def index(response):
	contenido = " OK "
	return HttpResponse(contenido)
def matrixOperations(response):
	contenido = "Operacion con Matrices"
	return HttpResponse(contenido)