'''
Manipulando strings
* String indices
* Fatiamento de string [inicio:fim"passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
'''

# Indices Positivos   [012345678]
texto               = 'Python_s2'
print(texto[2])  # Pega o caractere na posição 2
print(texto[:5])  # Pega o caractere do Inicio até o 4
print(texto[7:])  # Pega o caractere do 7 até o Final
print(texto[0:6:2])  # Pega o caractere do Inicio até o 5 pulando de 2 em 2

# Indices Negativos  -[987654321]
texto               = 'Python_s2'
print(texto[-2])
print(texto[-8:-2])
print(texto[:-1])