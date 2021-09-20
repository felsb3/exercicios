# Estrutura Sequencial exercício 11 https://wiki.python.org.br/EstruturaSequencial
# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
nReal = int(input('Digite o numero Real: '))
r1 = n1 * 2 * (n2 / 2)
print(f'O produto do dobro do primeiro com metade do segundo = {r1}')
r2 = n1 *  3 + nReal
print(f'A soma do triplo do primeiro com o terceiro = {r2}')
r3 = nReal ** 3
print(f'O terceiro elevado ao cubo= {r3}')
