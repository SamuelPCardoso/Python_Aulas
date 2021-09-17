'''
While/Else
Contadores e Acumuladores
'''

'''
contador = 1

while contador <= 50:
    print(contador)
    contador += 1  # contador = contador + 1
'''

'''
contador = 1
acumulador = 1

while contador <= 50:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Acabou no Else!')
'''

contador = 1
acumulador = 1

while contador <= 50:
    print(contador, acumulador)

    if contador > 10:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('Não será executado!')
print('Será executado!')
