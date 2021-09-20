# Estrutura Sequencial exercício 6 https://wiki.python.org.br/EstruturaSequencial
# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
r = float(input('Digite o raio do Circulo em metros:  '))
a = math.pi*pow(r, 2)
print(f'A área do circulo é {a} m²')
