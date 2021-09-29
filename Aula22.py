'''
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
'''
'''
    # É como se fosse uma variável, mas contem vários valores. Pode se colocar qualquer coisa dentro de uma lista.
    lista0 = [1, 2, 3, 4, 'Str', True, ]


    #         0    1    2    3    4
    lista = ['A', 'B', 'C', 'D', 'E']
    #        -5   -4   -3   -2   -1

    print(lista)
    print(lista[3])
    print(lista[-2])


    lista[2] = 'Olá'  # Altera valor dentro da lista
    print(lista)

    lista2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    print(lista2[1:9:2])  # Fatiamento da lista
    print(lista2[:9:2])  # Fatiamento da lista
    print(lista2[::2])  # Fatiamento da lista
    print(lista2[::-1])  # Fatiamento da lista
    print(lista2[0])  # Fatiamento da lista
    print(lista2[-1])  # Fatiamento da lista
'''
'''
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2

print(lista1)
print(lista2)
print(lista3)
'''

'''
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)  # Estende a lista
print(lista1)

lista2.append('c')  # Adiciona dados no final da lista
print(lista2)

lista3 = [7, 8, 9]
lista3.insert(1, 'Bola')  # Insere dados na lista onde você quer
print(lista3)

lista4 = ['A', 'B', 'C', 'D']
lista4.pop()  # Remove último dado da lista
print(lista4)

lista5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del(lista5[1:3])
del(lista5[5])  # Deleta dados em posições especificas
print(lista5)

lista6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(lista6))  # Mostra o maior dado
print(min(lista6))  # Mostra o menor dado

# Pode usar a função list para criar listas a partir de elementos interaveis, o range é uma função interavel
lista7 = list(range(0, 11))
print(lista7)

lista8 = [1, 2, 3, 4, 5, 6, 7]
for valor in lista8:
    print(valor)

lista9 = ['String', True, 10, -8.3]
for elementos in lista9:
    print(
        f'O tipo de elementos é {type(elementos)} e seu valor é {elementos}.')
'''

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Ahhh, isso não vale! Digite apenas uma letra!')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUUUULLL, a letra "{letra}" existe na palavra secreta!')
    else:
        print(f'Affff, a letra "{letra}" NÃO EXISTE na palavra secreta!')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f'Que legal, você acertou! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}.')

    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
