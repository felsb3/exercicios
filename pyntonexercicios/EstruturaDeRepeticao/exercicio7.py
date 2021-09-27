# Estrutura de repetição exercício 7 https://wiki.python.org.br/EstruturaDeRepeticao
# Faça um programa que leia 5 números e informe o maior número.

maximo = fliot(input('Digite um número: '))

for _ in range(4):
    maximo = max(maximo, float(input('digite um número: ')))
    print(f'Número máximo encontrado até agora é: {maximo}')
