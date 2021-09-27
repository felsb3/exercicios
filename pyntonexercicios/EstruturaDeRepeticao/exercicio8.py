# Estrutura de repetição exercício 7 https://wiki.python.org.br/EstruturaDeRepeticao
# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = float(input('Digite um número: '))

for n in range(2, 6):
    soma += float(input('digite um número: '))
    media = soma / n
    print(f'A soma dos números é: {soma}, e a média é {media}')
