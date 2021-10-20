'''
Funções - def em Python (Parte 1)
'''


def funcao():
    print('Hello World!')


def saudacao(msg='Olá', nome='usuário'):
    print(msg, nome)


saudacao('Oi', 'João')
saudacao()
saudacao(nome='Hello', msg='Jhon')


def saudacao_1(nome='Oi', msg='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'


variavel = saudacao_1
print(variavel)
