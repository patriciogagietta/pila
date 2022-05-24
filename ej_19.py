""" Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de es-
treno, desarrollar las funciones necesarias para resolver las siguientes actividades:

a. mostrar los nombre películas estrenadas en el año 2014;
b. indicar cuántas películas se estrenaron en el año 2018;
c. mostrar las películas de Marvel Studios estrenadas en el año 2016. """


from pila import Pila

class Peliculas(object):
    def __init__(self,titulo,estudio_cinematografico,anio_estreno):
        self.titulo = titulo
        self.estudio_cinematografico = estudio_cinematografico
        self.anio_estreno = anio_estreno


pila_peliculas = Pila()
pila_aux = Pila()


peli = Peliculas('shreck','marvel studios',2016)
pila_peliculas.apilar(peli)
peli = Peliculas('hombre araña','ashe',2018)
pila_peliculas.apilar(peli)
peli = Peliculas('batman','marvel studios',2016)
pila_peliculas.apilar(peli)
peli = Peliculas('busqueda implacable','ffffffff',2018)
pila_peliculas.apilar(peli)
peli = Peliculas('can','ffffffff',2018)
pila_peliculas.apilar(peli)


cont_peliculas = 0

#punto a
while(not pila_peliculas.pila_vacia()):
    dato = pila_peliculas.desapilar()
    if (dato.anio_estreno == 2014):
        print('pelicula estrenada en el anio 2014: ' ,dato.titulo)

    pila_aux.apilar(dato)

while(not pila_aux.pila_vacia()):
    pila_peliculas.apilar(pila_aux.desapilar())


#punto b
while(not pila_peliculas.pila_vacia()):
    dato = pila_peliculas.desapilar()
    if (dato.anio_estreno == 2016 and dato.estudio_cinematografico == 'marvel studios'):
        print('peliculas de marvel studios estrenadas en el 2016: ' ,dato.titulo)

    pila_aux.apilar(dato)

while(not pila_aux.pila_vacia()):
    pila_peliculas.apilar(pila_aux.desapilar())

#punto c
while(not pila_peliculas.pila_vacia()):
    dato = pila_peliculas.desapilar()
    if (dato.anio_estreno == 2018):
        cont_peliculas = cont_peliculas + 1

    pila_aux.apilar(dato)

while(not pila_aux.pila_vacia()):
    pila_peliculas.apilar(pila_aux.desapilar())


print('cantidad de peliculas estrenadas en el 2018: ' ,cont_peliculas)
