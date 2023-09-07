import random

print ("Bienvenidos al juego de Piedra, Papel o Tijeras hecho por Samuel")
usuario = int (input ("¿Qué opción quieres?. Escribe 0 para piedra, 1 para papel y 2 para tijeras "));

ordenador = random.randint (0,2)

print ("Usuario = " + str (usuario))

print (f"Ordenador = {ordenador}")

if usuario == 0 and ordenador == 2:
    print ("Ha ganado el usuario");

elif usuario > ordenador:
    print ("Ha ganado el usuario");

elif usuario == ordenador:
    print ("Empate");

else:
    print ("Ha ganado el ordenador");





