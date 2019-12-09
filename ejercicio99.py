# Ejercicio 99
#Escriba un programa que permita al usuario convertir un número de una base a otra. 
#Su programa debe admitir bases entre 2 y 16 tanto para el número de entrada como para el número de resultado. 
#Si el usuario elige una base fuera de este rango, se debe mostrar un mensaje de error apropiado y el programa debe salir. 
#Divida su programa en varias funciones, incluida una función que convierte de una base arbitraria a una base 10, 
#una función que convierte de una base 10 a una base arbitraria y un programa principal que lee las bases y el número de entrada del usuario.
#Puede encontrar sus soluciones a los ejercicios 77, 78 y 98 útiles al completar este ejercicio.

from ejercicio98 import *

def dec2n(num, new_base):
    result = ' '
    q = num

    r = q % new_base
    result = int2hex(r) + result
    q = q // new_base

    while q > 0:
        r = q % new_base
        result = int2hex(r) + result
        q = q // new_base

    return result
def n2dec(num, b):
    decimal = 0
    power = 0

    for i in range(len(num)):
        decimal = decimal * b
        decimal = decimal + hex2int(num[i])
    return decimal
def main():
    from_base = int (input('Introduce la base convertida por: '))
    from_num = input('Introduce la secuencia de digitos en esta base')

dec = n2dec(from_num, from_base)
print('esto es %d en base 10.' %dec)

to_base = int(input('Introduce la base a convertir a: '))
to_num = dec2n(dec, to_base)
print('esta es %s en base %d ' %(to_num, to_base))