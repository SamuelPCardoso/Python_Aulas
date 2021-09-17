'''
Variável:
Iniciar com letra, pode conter números, separar com _, letras minúsculas
'''

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua algura: '))
peso = float(input('Digite seu peso: '))
imc = peso / altura ** 2

print('{} tem {} anos de idade, seu peso é {} e sua altura {}. Seu IMC é {}.'.format(nome, idade, peso, altura, imc))
