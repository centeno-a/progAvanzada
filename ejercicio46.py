# Ejercicio 46
# El año esta dividido en cuatro temporadas: Primavera, Verano, otoño e invierno
# Aunque las fechas exacatas cambian un poco dependiendo del año, usemos las siguientes fechas:
# Temporada Primer dia
# Primavera Marzo      21
# Verano    Junio      21
# Otoño     Septiembre 22
# Invierno  Diciembre  21
# Escriba un programa en el que el usuario introduzca el mes y dia.
# El usuario introducira el nombre del mes como una 'string' seguido del dia como entero 'int'
# Su programa debe desplegar la temporada de acuerdo a la informacion introducida por el usuario.

mes = input('Introduce el mes: ')
dia = int(input('Introduce el dia: '))

if mes == 'enero' or mes == 'febrero':
    temporada = 'invierno'
elif mes == 'marzo' and dia <20:
    temporada = 'invierno'
elif mes == 'marzo' and dia >=21:
    temporada = 'primavera'
elif mes == 'abril' or mes == 'mayo':
    temporada = 'primavera'
elif mes == 'junio' and dia <20:
    temporada = 'primavera'
elif mes == 'junio' and dia >=21:
    temporada = 'verano'
elif mes == 'julio' or mes == 'agosto':
    temporada = 'verano'
elif mes == 'septiembre' and dia <21:
    temporada = 'otono'
elif mes == 'septiembre' and dia >=22:
    temporada = 'otono'
elif mes == 'octubre' or mes == 'noviembre':
    temporada = 'otono'
elif mes == 'diciembre' and dia <20:
    temporada = 'ivierno'
elif mes == 'diciembre' and dia >=21:
    temporada = 'invierno'

print(mes, dia, 'es en ', temporada)
