""" Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
necesarias para resolver las siguientes actividades:

a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
ción uno la cima de la pila;
b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
car la cantidad de películas en la que aparece;
c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
d. mostrar todos los personajes cuyos nombre empiezan con C, D y G. """


from pila import Pila


class Personajes_Marvel (object):
    def __init__(self,nombre,cantidad_pelicula):
        self.nombre = nombre
        self.cantidad_pelicula = cantidad_pelicula

pila_personajes = Pila()
pila_aux = Pila()

personaje = Personajes_Marvel('capitan america',8)
pila_personajes.apilar(personaje)
personaje = Personajes_Marvel('rocket raccoon',1)
pila_personajes.apilar(personaje)
personaje = Personajes_Marvel('viuda negra',2)
pila_personajes.apilar(personaje)
personaje = Personajes_Marvel('groot',2)
pila_personajes.apilar(personaje)
personaje = Personajes_Marvel('thor',10)
pila_personajes.apilar(personaje)

cont_viuda = 0

#punto a
j = pila_personajes.cima()

for j in range (pila_personajes.tamanio()):
    dato = pila_personajes.desapilar()
    if (dato.nombre == 'rocket raccoon'):
        print('posicion que se encuantra rocket raccoon: ',j)

    if (dato.nombre == 'groot'):
        print('posicion que se encuantra groot: ',j)
            
    pila_aux.apilar(dato)


while(not pila_aux.pila_vacia()):
    pila_personajes.apilar(pila_aux.desapilar())

#punto b
while(not pila_personajes.pila_vacia()):
    dato = pila_personajes.desapilar()
    if (dato.cantidad_pelicula > 5 ):
        print(dato.nombre , 'participo en mas de 5 peliculas, total en las que participo: ',dato.cantidad_pelicula)
    
    pila_aux.apilar(dato)

while(not pila_aux.pila_vacia()):
    pila_personajes.apilar(pila_aux.desapilar())

#punto c
while(not pila_personajes.pila_vacia()):
    dato = pila_personajes.desapilar()
    if (dato.nombre == 'viuda negra'):
        cont_viuda = cont_viuda + 1

    pila_aux.apilar(dato)

print('cantidad de peliculas en la que participo la viuda negra: ',cont_viuda)

while(not pila_aux.pila_vacia()):
    pila_personajes.apilar(pila_aux.desapilar()) 


#punto d
