numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero = int(numero)

    if numero % 2 == 0:
        print(f'Você digitou {numero}, que é um número PAR!')
    else:
        print(f'Você digitou {numero}, que é um número ÍMPAR.')
else:
    print('Isso não é um número inteiro!')


'''

CHECAGEM INVERTIDA:

numero = input('Digite um número inteiro: ')

if not numero.isdigit():
    print('Isso não é um número inteiro')
else:
    numero = int(numero)

    if not numero % 2 == 0:
        print('Número é ÍMPAR!')
    else:
        print('Número é PAR!')

'''