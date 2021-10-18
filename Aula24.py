'''
Desempacotamento de listas em Python
'''

lista = ['Luiz', 'João', 'Maria']

n1, n2, n3 = lista

# n1, n2, *nome_da_variavel = lista  -  caso tenha mais valores e não queremos
# mostrar
# *nome_da_variavel, n1, n2, n3 - desempacota de trás para frente

print(n2)
