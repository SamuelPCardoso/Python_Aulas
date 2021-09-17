"""
Tipos de dados Primitivos:
str - string: textos "Assim" ou 'Assim'
int - inteiro: 123456 - 0 -10 -20 -50 -60 -15000 1500
float - real/pont flutuante: 10.50 1.5 -10.3 -50.93 0.3 
bool - booleano/lógico: True ou False
"""

print('Samuel', type('Samuel'))
print(10, type(10))
print(25.3, type(25.3))
print(10 == 10, type(10 == 10))
print('Oi' == 'Oi', type('Oi' == 'Oi'))
print(5 == 10, type(5 == 10))
print('Oi' == 'Oe', type('Oi' == 'Oe'))

# Converter tipos de dados:
print('Samuel', type('Samuel'), bool('Samuel'))
print('10', type('10'), type(int('10')))

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))

print('Seu nome é {}'.format(nome), type(nome))
if idade >= 18:
    print('Você tem {} anos e você é maior de idade!'.format(idade), type(idade))
else:
    print('Você tem {} anos e você é menor de idade!'.format(idade), type(idade))

print('Sua altura é {}'.format(altura), type(altura))
