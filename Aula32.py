'''
Funções (def) em Python - return - (Parte 2)
'''

'''
def funcao(var):
    return var
    print('Isso não será executado.')


variavel = funcao('Valor que eu quero.')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')
'''


def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2


'''
def divisao(n1, n2):
    if n2 == 0:
        return
    
    return n1 / n2
'''


v1 = int(input('Digite um valor: '))
v2 = int(input('Digite um valor: '))
divide = divisao(v1, v2)

if divide:
    print(divide)
else:
    print('Conta inválida')
