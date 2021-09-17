#        Índices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'  # Iterável
tamanho_frase = len(frase)
contador = 0
nova_strig = ''
print(frase)
input_do_usuario = input('Qual letra você quer por maiúsculo: ')

'''
while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1
'''

'''
while contador < tamanho_frase:
    nova_strig += frase[contador]
    print(nova_strig)
    contador += 1
'''

'''
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'r':
        nova_strig += 'R'
    else:
        nova_strig += letra
    contador += 1

print(nova_strig)
'''

# Iteração -> Iterar  ==  Ato de percorer cada elemento Iterável
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_strig += input_do_usuario.upper()
    else:
        nova_strig += letra
    contador += 1
print(nova_strig)
