# Ejercicio 43
# Es común que las imágenes de los líderes anteriores de un país, u otras personas de importancia histórica, aparezcan en su dinero. 
# Las personas que aparecen en los billetes en los Estados Unidos son las siguientes.
# Escriba un programa que comience leyendo la denominación de un billete del usuario. 
# Luego, su programa debe mostrar el nombre de la persona que aparece en el billete de la cantidad ingresada. 
# Se debe mostrar un mensaje de error apropiado si no existe dicha cantidad.

denominacion = int(input("Introduce la denominacion de un billete: $"))

nombre = ""

if denominacion == 1:
	nombre = "George Washington"
if denominacion == 2:
	nombre = "Thomas Jefferson"
if denominacion == 5:
	nombre = "Abraham Lincoln"
if denominacion == 10:
	nombre = "Alexander Hamilton"
if denominacion == 20:
	nombre = "Andrew Jackson"
if denominacion == 50:
	nombre = "Ulysses S. Grant"
if denominacion == 100:
	nombre = "Benjamin Franklin"
	
if nombre == "":
	print("Esa cantidad es incorrecta, intenta de nuevo.")
else:
	print("La persona de la denomicacion es: ",(nombre))
