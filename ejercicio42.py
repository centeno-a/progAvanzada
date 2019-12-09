## Ejercicio 42
# En la pregunta anterior, convertiste del nombre de la nota a la frecuencia. 
# En esta pregunta escribirás un programa que revierte ese proceso. 
# Comience leyendo una frecuencia del usuario. 
# Si la frecuencia está dentro de un Hertz de un valor que figura en la tabla de la pregunta anterior, informe el nombre de la nota. 
# De lo contrario, informe que la frecuencia no corresponde a una nota conocida. 
# En este ejercicio solo necesita considerar las notas enumeradas en la tabla. 
# No hay necesidad de considerar notas de otras octavas.

frequencia = float(input('Introsuce la frecuencia en Hz:  '))

nota = ""

if frequencia > 261.63 - 1 and frequencia < 261.63 + 1:
	nota = "C"
elif frequencia > 293.66 - 1 and frequencia < 293.66 + 1:
	nota = "D"
elif frequencia > 329.63 - 1 and frequencia < 329.63 + 1:
	nota = "E"
elif frequencia > 349.23 - 1 and frequencia < 349.23 + 1:
	nota = "F"
elif frequencia > 392.00 - 1 and frequencia < 392.00 + 1:
	nota = "G"
elif frequencia > 440.00 - 1 and frequencia < 440.00 + 1:
	nota = "A"
elif frequencia > 493.88 - 1 and frequencia < 493.88 + 1:
	nota = "B"
	
if nota == "":
	print('No es una nota conocida')
else:
	print('Esta es una nota',(nota))
