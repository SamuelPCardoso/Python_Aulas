'''
Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne fizz, se o parâmetro da 
função for divisível por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e por 3, 
retorne FizzBuzz, caso contrário, retorne o número enviado.
'''

import random


def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    if n % 5 == 0:
        return 'Buzz'
    if n % 3 == 0:
        return 'Fizz'
    return n


print(fb(3))
print(fb(5))
print(fb(10))
print(fb(12))
print(fb(15))
print(fb(7))
