# Estrutura
# de
# Decisão
# Exercicio
# 3
#
# [7]
# True, False
# print(5 < 6)
#
# [8]
# sexo = input('Digite aqui seu sexo "M" para masculino "F" para feminino e "I" para não definir: ').upper()
# if sexo == 'M':
#     print('Masculino')
# elif sexo == "F":
#     print('Feminino')
# elif sexo == "I":
#     print('Indefinido')
# else:
#     print('sexo invalido')
# print('Finalizou o programa')
# []
# 0
# s
# nota_1 = float(input('digite sua nota: '))
# nota_2 = float(input('digite sua nota: '))
# media = (nota_1 + nota_2) / 2
# print(f'Sua média foi: {media}')
# if media >= 10:
#     print('Aprovado com distinção')
# elif media >= 7:
#     print('Aprovado')
# else:
#     print('Reprovado')
# []
# 0
# s
# numero = int(input('digite um número: '))
# centenas_str = dezenas_str = unidades_str = ''
#
# centenas_int, numero = divmod(numero, 100)
#
# partes_numericas = 0
#
# if centenas_int == 1:
#     centenas_str = '1 centena'
#     partes_numericas += 1
#
# []
# 0
# s
# []
# 0
# s
# saldo = int(input())
# taxa = 1.00347
# anos = 0
# while saldo < 1000:
#     # print (anos)
#     # print (saldo)
#     anos += 1
#     saldo *= taxa
#
# print(anos)
#
# Faça
# um
# Programa
# que
# peça
# a
# temperatura
# em
# graus
# Fahrenheit, transforme
# e
# mostre
# a
# temperatura
# em
# graus
# Celsius.C = 5 * ((F - 32) / 9).
#
# acessar
# o
# site
# []
# 0
# s
# while True:
#     try:
#         numero = int(input('informe um numero de 0 a 10: '))
#     except ValueError:
#         print('fornessa um valor inteiro')
#     else:
#         if 0 <= numero <= 10:
#             print(f'numero informado {numero}')
#             break
#         else:
#
# []
# 0
# s
# tabuada = int(input('Tabuada de: '))
# for i in range(1, 11, 1):
#     x = tabuada * i
#     print(f'{tabuada} x {i} = {x}')
# []
# 0
# s
# maximo = float(input('Digite um número: '))
#
# for _ in range(5):
#     maximo += float(input('Digite um número: '))
#     print(f'Sua soma é: {maximo}')
#     print(f'E sua média é: {maximo / 2}')
# []
# 0
# s
# x = "awesome"
#
#
# def myfunc():
#     global x
#     x = "fantastic"
#     print(x)
#
#
# print('###')
# print(myfunc())
# print('###')
# myfunc()
#
# []
# 0
# s
#
#
# def enes(n):
#     for c in range(1, n + 1):
#         cont = 1
#         while True:
#             print(c, end=' ')
#             if cont == c:
#                 break
#             cont += 1
#         print()
#
#
# []
# 0
# s
#
#
# def exercicio_1(n):
#     for i in range(n):
#         i += 1
#         print(str(i) * i)
#
#
# n = int(input('Digite um número: '))
# exercicio_1(n)
# [2]
# 0
# s
#
#
# def converta(h, m):
#     if 0 < h <= 12 and 0 < m < 60:
#         print(f'{h}:{m} AM')
#     elif 12 < h < 24 and 0 < m < 60:
#         print(f'{h - 12}:{m} PM')
#     else:
#         print('Valor inválido')
#
#
# while True:
#
# [6]
# 0
# s
#
#
# def valorPagamento(p, d):
#     return p * 1.03 + 0.001 * d
#
#
# c = t = 0
#
# while True:
#     p = float(input('Valor da prestação: '))
#     if p == 0:
#         print(f'Total: {t}. Quantidade: {c} ')
#         break
#
# [5]
# 0
# s
#
#
# def ret(l, a):
#     if l > 20:
#         l = 20
#     if a > 20:
#         a = 20
#     print('-o-' * l)
#     c = 0
#     while c < a:
#         z = '|'
#         print(f'{z}{z:>{(l * 3 - 1)}}')
#
#
# [4]
# 0
# s
# import random
#
# a1 = str(input('Primeiro aluno: '))
# a2 = str(input('Segundo aluno: '))
# a3 = str(input('Terceiro aluno: '))
# a4 = str(input('Quarto aluno: '))
# print('Sorteio: {}'.format(random.choice([a1, a2, a3, a4])))
# print('\033[0;30;41mOlá, Mundo\033[m')
from random import choices

qtd = 1
tamanho = 6
valores = range(1, 60)

listas = [choices(valores, k=tamanho) for _ in range(qtd)]
print(listas)

import random

i = 0

while i < 6:
    print(random.randrange(1, 60))
    i += 1

menu = {1: 'Converter de °C para °F', 2: 'Converter de °F para °C', 3: 'Exit'}
option = 0
for key, value in menu.items():
    print(key, value)
    option = int(input("Escolha uma opção 1: 'Converter de °C para °F', 2: 'Converter de °F para °C', 3: 'Exit': "))
    if option == 1:
        C = float(input('Digite aqui a temperatura em Celsius: '))
        Fahrenheit = ((C / 5) * 9) + 32
        print(f'{float(Fahrenheit)}° graus Fahrenheit')
    elif option == 2:
        f = float(input('Digite a temperatura em (°F): '))
        celsius = 5 * ((f - 32) / 9)
        print(f'Temperatura em (°C) = {celsius} ')
    elif option == 3:
        print('Você saiu do programa')
