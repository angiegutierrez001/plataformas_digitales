# programa que verifica si una palabra es palindromo

palabra = input('Ingrese una palabra para verificar si es palindromo \n')

if (palabra == palabra[::-1]):
    print('Es palindromo')
else:
    print('No es palindromo')



