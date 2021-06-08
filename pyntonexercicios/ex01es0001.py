# Estrutura Sequencial exercício 1 https://wiki.python.org.br/EstruturaSequencial
# 1 Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print('Olá Mundo')
# 2 Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = int(input('Informe seu número: '))
print(f'O número informado foi {numero}.')
# 3 Faça um Programa que peça dois números e imprima a soma.
numeroA = int(input('Informe o primeiro número: '))
numeroB = int(input('Informe o segundo número: '))
soma = numeroA + numeroB
print(f'O resultado da soma é: {soma}')
# 4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota_1 = float(input('Digite sua primeira nota: '))
nota_2 = float(input('Digite sua segundo nota: '))
nota_3 = float(input('Digite sua terciro nota: '))
nota_4 = float(input('Digite sua quarta nota: '))
meida = (nota_1 + nota_2 + nota_3 + nota_4)/4
print(f'Sua média foi: {meida}')
# 5 Faça um Programa que converta metros para centímetros.
tamanho_em_metros = float(input('Incisa um valor em metros: '))
tamanho_em_centimetros = tamanho_em_metros * 100
print (f'Seu valor é igual a {tamanho_em_centimetros} cm')
print()

c = float (input('Insira os centímetros a serem convertidos:  '))
r = c / 100
print (f'{c} cm, é equivalente a: {r} metros')
