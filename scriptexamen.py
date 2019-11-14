#escribir un programa donde dados dos valores enteros insertados por el usuario desplegar su producto,si su producto es mayor de 1000 desplegar tambien su suma
valor1 = int(input('introducir un valor entero:'))
valor2 = int(input('introducir un valor entero:'))


multiplicacion =valor1 * valor2
print('el total es',multiplicacion)


if multiplicacion > 1000:
    suma = valor1 + valor2
    print('la suma del valor 1 + la suma del valor2 es:',suma)



elif multipliocacion <1000:
     print ('el producto es menor a 1000:')
