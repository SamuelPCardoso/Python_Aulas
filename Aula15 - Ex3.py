nome = input('Digite seu nome: ')
nome_len = len(nome)

if nome_len <= 4:
    print('Seu nome é curto!')
elif nome_len <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é grande!')
