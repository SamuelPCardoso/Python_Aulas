nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua algura: '))
peso = float(input('Digite seu peso: '))
imc = peso / altura ** 2

print('{} tem {} anos de idade, seu peso é {} e sua altura {}. Seu IMC é {:.2f}.'.format(nome, idade, peso, altura, imc))
print(f'{nome} tem {idade} anos de idade, seu peso é {peso} e sua altura {altura}. Seu IMC é {imc:.2f}.')

print('{0} tem {1} anos de idade, seu peso é {2} e sua altura {3}. Seu IMC é {4:.2f}.'.format(nome, idade, peso, altura, imc))
print('{3} {0} {1} tem {1} anos de idade, seu peso é {2} e sua altura {3}. Seu IMC é {4:.2f}.'.format(nome, idade, peso, altura, imc))

print('{a} tem {h} anos de idade, seu peso é {f} e sua altura {c}. Seu IMC é {e:.2f}.'.format(a=nome, h=idade, f=peso, c=altura, e=imc))
