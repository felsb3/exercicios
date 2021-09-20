# Estrutura Sequencial exercício 8 https://wiki.python.org.br/EstruturaSequencial
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
salario_hora = int(input('Informe seu salário por hora: '))
horas_no_mes = int(input('Informe quantas horas vc trabalhou no mês: '))
salario_mes = salario_hora * horas_no_mes
print(f'Seu salário do mês foi: R$ {salario_mes}.')
