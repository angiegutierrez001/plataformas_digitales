#ingrese un numero y diga si es par o impar
"""dotstring
1. pedir al usuario ingresar un numero
2. hacer el calculo para ver si es par o impar (variable % 2 == 0 es par)
3. mostrar el mensaje
"""
numero = int(input('Por favor ingrese un numero '))

if (numero == 0):
    print('Valor neutral')
elif numero % 2 == 0:
    print("Su numero es par")
else:
    print("Su numero es impar")



