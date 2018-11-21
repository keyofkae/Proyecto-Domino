#Práctica8-Proyecto Dominó-Luis Contell,Carlos Palencia,Dani Cabot-1ºDAW
#Creamos la lista de todas las fichas que hay
import random
fichastotales=["[0|0]","[0|1]","[0|2]","[0|3]","[0|4]","[0|5]","[0|6]","[1|1]","[1|2]","[1|3]","[1|4]","[1|5]","[1|6]","[2|2]","[2|3]","[2|4]","[2|5]","[2|6]","[3|3]","[3|4]","[3|5]","[3|6]","[4|4]","[4|5]","[4|6]","[5|5]","[5|6]","[6|6]"]
aleatorio=random.choice(fichastotales)
fichasjugador1=[]
fichasjugador2=[]
contador=0
while contador<14:
    aleatorio=random.choice(fichastotales)
    fichasjugador1.append(aleatorio)
    fichastotales.remove(aleatorio)
    fichasjugador2=fichastotales
    contador=contador+1
#Programa pregunta los nombres de los  jugadores
jugador1=input("Nombre jugador1:")
jugador2=input("Nombre jugador2:")
#Comienza el juego
print("Comienza el juego,suerte jugadores")
print("Jugador 1:",fichasjugador1)
print("Jugador 2:",fichasjugador2)

