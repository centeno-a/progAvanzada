# Ejercicio 47
# Los horóscopos 





j
mes = int(input('Introduce el mes de tu nacimiento: '))
dia = int(input('Introduce el dia de tu nacimiento: '))

mes <= 12 and mes >= 1
dia <= 31 and mes >= 1


zodiaco = ""

if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
	zodiaco = "Capricornio"
	
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
	zodiaco = "Aquario"
	
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
	zodiaco = "Piscis"
	
elif (mes == 3 and dia >= 21) or (mes == 4 and dai <= 19):
	zodiaco = "Aries"
	
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
	zodiaco = "Tauro"

elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
	zodiaco = "Geminis"
	
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
	zodiaco = "Cancer"
	
elif (mes == 7 and dia <= 23) or (mes == 8 and dia <= 22):
	zodiaco = "Leo"
	
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
	zodiaco = "Virgo"
	
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
	zodiaco = "Libra"
	
elif (mes == 10 and dia <= 23) or (mes == 11 and dia <= 21):
	zodiaco = "Escorpion"
	
elif (mes == 11 and dia <= 22) or (mes == 12 and dia <= 21):
	zodiaco = "Sagitario"
    
	
print('Tu signo zodiacal es:  ',(zodiaco))
