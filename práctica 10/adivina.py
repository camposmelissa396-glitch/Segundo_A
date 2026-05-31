import random

def tirar_dados():
 return random.randint(2, 12)

def pedir_respuestas():
 print("Ingresar tu prediccion")
 print("1. par")
 print("2.impar")
 print("3. salir del juego")

 return int(input())

def imprimir_resultado(numero, prediccion):
 pass

while True:
 numero = tirar_dados()
 prediccion = pedir_respuestas()
 if prediccion == 3:
  break
 imprimir_resultado(numero, prediccion)

 print("Gracias por jugar")

 #print("Tiro de datos:", tirar_datos())

