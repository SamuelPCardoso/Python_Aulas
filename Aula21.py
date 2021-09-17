'''
For in  em  Python
Iterando strings com For
Função range(start = 0, stop, step = 1)
'''

texto = 'Python'
for letra in texto:
    print(letra)
print('-*-' * 5)
texto = 'Python'
for n, letra in enumerate(texto):
    print(n, letra)
print('-*-' * 5)
for numero in range(10):
    print(numero)
print('-*-' * 5)
#                start    stop    step
for num in range(1,       17,     2):
    print(num)
print('-*-' * 5)
#                start    stop    step
for num_inv in range(20,       10,     -1):
    print(num_inv)
print('-*-' * 5)
for num_rest in range(100):
    if num_rest % 8 == 0:
        print(num_rest)
print('-*-' * 5)

texto_velho = 'Python'
nova_string = ''

#  continue  ==  pula para o proximo laço
#  break  ==  termina o laço

for palavra in texto_velho:
    if palavra == 't':
        nova_string = nova_string + palavra.upper()
    elif palavra == 'h':
        nova_string += palavra.upper()
    else:
        nova_string += palavra
print(nova_string)
