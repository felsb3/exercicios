# Estrutura De Decisão exercício 1 https://wiki.python.org.br/EstruturaDeDecisao
# Faça um Programa que peça dois números e imprima o maior deles.

nunero1 = int(input('Inserir o primeiro número: '))
nunero2 = int(input('inserir o segundo número: '))
if nunero1 >= nunero2:
    print(f'O maior deles é: {nunero1}')
else:
    print(f'O maior deles é: {nunero2}')

