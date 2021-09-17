'''
Podemos usar a função -len- para contar caracteres
'''

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print(f'O nome {usuario} tem {qtd_caracteres} caracteres.')

if qtd_caracteres >= 5:
    print('Você pode se cadastrar!')
else:
    print('Digite um usuário com 5 ou mais caracteres.')

'''
string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra alguma coisa: ')

print(f'A quantidade total de caraccteres digitados foi {len(string1) + len(string2)}')

print(len(string1)) == print(string1.__len__())

len não funciona com int, float e bool  -  print(len(123456)) == ERROR

Em Python TUDO É OBJETO

'''