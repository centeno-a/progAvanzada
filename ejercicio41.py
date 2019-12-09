## Ejercicio 41
# Comience escribiendo un programa que lea el nombre de una nota del usuario y muestre la frecuencia de la nota. 
# Su programa debe admitir todas las notas enumeradas anteriormente.
# Una vez que tenga su programa funcionando correctamente para las notas enumeradas anteriormente, 
# debe agregar soporte para todas las notas de C0 a C8. 
# Si bien esto podría hacerse agregando muchos casos adicionales a su declaración if, 
# dicha solución es engorrosa, poco elegante e inaceptable para los propósitos de este ejercicio. 
# En cambio, debe explotar la relación entre las notas en octavas adyacentes. 
# En particular, la frecuencia de cualquier nota en octava “n” es la mitad de la frecuencia de la nota correspondiente en octava n + 1. 
# Al usar esta relación, debería poder agregar soporte para las notas adicionales sin agregar casos adicionales a su declaración if.

nombre = input('Inserta el nombre de la nota: ')


nota = nombre[0].upper()

octave = int(nombre[1])

frequencia = -1

if nota == "C":
	frequencia = 261.63
elif nota == "D":
	frequencia = 293.66
elif nota == "E":
	frequencia = 329.63
elif nota == "F":
	frequencia = 349.23
elif nota == "G":
	frequencia = 392.00
elif nota == "A":
	frequencia = 440.00
elif nota == "B":
	frequencia = 493.88
	
frequencia /= 2 ** (4 - octave) 
	
print('La nota es:' ,nota, 'frequencia es ',(frequencia), 'Hz')


