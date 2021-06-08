# 6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
r = float(input('Digite o raio do Circulo em metros:  '))
a = math.pi*pow(r, 2)
print(f'A área do circulo é {a} m²')
# 7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lateral = int(input('informe o tamanho da lateral do quadrado: '))
dobro_da_area = (lateral * lateral)*2
print(f'O dobro de sua area é {dobro_da_area}')
# 8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês.
salario_hora = int(input('Informe seu salário por hora: '))
horas_no_mes = int(input('Informe quantas horas vc trabalhou no mês: '))
salario_mes = salario_hora * horas_no_mes
print(f'Seu salário do mês foi: R$ {salario_mes}.')
# 9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).
F = float(input('Digite aqui a temperatura em Fahrenheit: '))
Ce = 5 * ((F-32) / 9)
print(f'{float(Ce)}')
# 10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
C = float(input('Digite aqui a temperatura em Celsius: '))
prova = ((C/5)*9)+32
print(f'{float(prova)}°')
# 11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
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
# 12 Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a
# seguinte fórmula: (72.7*altura) - 58
altura = float(input('Informe sua altura em metros: '))
peso_ideal = (72.7 * altura) - 58
print(f'Seu peso ideal é {peso_ideal} kg')
