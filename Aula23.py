'''
Split, Join, Enumerate em Python
* Split - Dividir uma string (str)
* Join - Junta uma lista mas também é uma função de str
* Enumerate - Enumerar elementos da lista # iteráveis
'''

'''
    string = 'O Brasil é o país do futebol, o Brasil é penta.'
    lista_1 = string.split(' ')
    lista_2 = string.split(',')

    print(lista_1)
    print(lista_2)
    print()

    for valor in lista_1:
        print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')
    print()

    palavra = ''
    contagem = 0
    for valor in lista_1:
        qtd_vezes = lista_1.count(valor)

        if qtd_vezes > contagem:
            contagem = qtd_vezes
            palavra = valor

    print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x).')
    print()

    for valor in lista_2:
        print(valor.strip())
'''

'''
    lista_1 = ['O', 'Brasil', 'é', 'Penta']
    print(lista_1)
    lista_2 = ','.join(lista_1)
    print(lista_2)
'''

lista = [
    [0, 'Pedro'],
    [1, 'Maria'],
    [2, 'José'],
]

for indice, nome in lista:  # Isto é o que a função enumerate faz
    print(indice, nome)

print()

lista = ['Pedro', 'Maria', 'José']

for indice, nome in enumerate(lista):
    print(indice, nome)
