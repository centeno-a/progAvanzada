# Ejercicio 45
# Las posiciones en un tablero de ajedrez se identifican con una letra y un número. 
# Escriba un programa que lea una posición del usuario. 
# Use una declaración if para determinar si la columna comienza con un cuadrado negro o un cuadrado blanco. 
# Luego use la aritmética modular para informar el color del cuadrado en esa fila. 
# Por ejemplo, si el usuario ingresa a1, su programa debe informar que el cuadrado es negro. 
# Si el usuario ingresa d5, entonces su programa debe informar que el cuadrado es blanco. 
# Su programa puede asumir que siempre se ingresará una posición válida. 
# No necesita realizar ninguna comprobación de errores.

posi = input('Introduce la posicion en el tablero: ')

columna = posi[0].lower()
fila = int(posi[1])

if columna in "wgitw":
	columnaempiezanegro = True
else:
	columnaempiezanegro = False
	
	
if columnaempiezanegro:
	if fila % 2 == 0:
		blanco = True
	else:
		blanco = False
else:
	if fila % 2 == 0:
		blanco = False
	else:
		blanco = True
		
if blanco:
	print('La posicion es el cuadro blanco')
else:
	print('La posicion es el cuadro negro')


