# Ejercicio 44
# Canadá tiene días tres feriados nacionales que caen en las mismas fechas cada año. 
# Escriba un programa que lea un mes y un día del usuario. 
# Si el mes y el día coinciden con uno de los feriados enumerados anteriormente, entonces su programa debería mostrar el nombre del feriado. 
# De lo contrario, su programa debería indicar que el mes y el día ingresados no corresponden a un día festivo de fecha fija.

fecha = input('Introduce el mes: ')
dia = int(input('Introduce el dia: '))


celebracion = ''

if fecha ==  'enero' and dia == 1:
    print('La celebracion es Año Nuevo')
elif fecha == 'julio' and dia == 1:
    print('La celebracion es Dia de Canada')
elif fecha == 'diciembre' and dia == 25: 
    print('La celebracion es Navidad')

else:
    print('La fecha es incorrecta')