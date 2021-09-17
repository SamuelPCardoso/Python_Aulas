'''
Formatando valores com modificadores

:s  -  Texto (str)
:d  -  Inteiros (int)
:f  -  Números de ponto flutuante (float)
:.(NÚMERO)f  -  Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)
>  -  Esquerda
<  -  Direita
^  -  Centro
'''


nome = 'Samuel'
print(nome)
print('{:#^20}'.format(nome))
print(f'{nome:#^20}')



num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print(divisao)
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')



test1 = 8
test2 = 45
test3 = 868
print(f'{test1:0>11}')
print(f'{test2:0<11}')
print(f'{test3:0^11}')