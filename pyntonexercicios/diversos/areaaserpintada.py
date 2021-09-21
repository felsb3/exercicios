import math

area_a_ser_pintada = int(input ('digite a área, em metros quadardos a ser pintada: ')) # area em metros quadrados
area_com_folga = area_a_ser_pintada * 1.1
litros_por_metro = 6
litros_a_serem_usados = area_com_folga / litros_por_metro
litros_por_lata = 18
numero_de_latas = math.ceil(litros_a_serem_usados / litros_por_lata)
valor_com_apenas_latas = numero_de_latas * 80
print (f'Você deverá usar {numero_de_latas} latas de 18 litros, no valor de R$ {valor_com_apenas_latas}')

litros_por_galao = 3.6
nunero_de_galoes = math.ceil(litros_a_serem_usados / litros_por_galao)
valor_com_apenas_galoes = nunero_de_galoes * 25
print (f'Você deverá usar {nunero_de_galoes} galões de 3.6 litros no valor de R$ {valor_com_apenas_galoes}')

# compra de tintas otimiada por valor
numero_de_latas = math.floor(litros_a_serem_usados / litros_por_lata)
valor_de_latas = numero_de_latas * 80
litros_faltantes = litros_a_serem_usados % litros_por_lata
nunero_de_galoes = math.ceil(litros_faltantes / litros_por_galao)
valor_com_galoes = nunero_de_galoes * 25

valor_total = valor_de_latas + valor_com_galoes

print (f'Você deverá usar {numero_de_latas} latas de 18 litros {nunero_de_galoes} galões de 3.6 litros, no valor de R$ {valor_total}')


area_a_ser_pintada = int(input ('digite a área, em metros quadardos a ser pintada: ')) # area em metros quadrados
valor_da_lata = 80
valor_do_galoes = 25
area_com_folga = area_a_ser_pintada * 1.1
rendimento_por_litro = 6
litros_a_serem_usados = area_com_folga / rendimento_por_litro
litros_por_lata = 18
numero_de_latas = math.ceil(litros_a_serem_usados / litros_por_lata)
valor_com_apenas_latas = numero_de_latas * valor_da_lata
print (f'''Você pode usar {numero_de_latas} latas de 18 litros no total de R$ {valor_com_apenas_latas}
       ''')

litros_por_galoes = 3.6
numero_de_galoes = math.ceil(litros_a_serem_usados / litros_por_galoes)
valor_com_apenas_galoes = numero_de_galoes * valor_do_galoes
print (f'Ou você pode usar {numero_de_galoes} latas de 3.6 litros no total de R$ {valor_com_apenas_galoes}')

print ('''
Ou usar o resultado otimizado:
''')
numero_de_latas = math.floor(litros_a_serem_usados / litros_por_lata)
valor_de_latas = numero_de_latas * valor_da_lata
print (f'Você deverá usar {numero_de_latas} latas de 18 litros no total de R$ {valor_de_latas}')
litors_faltantes = (litros_a_serem_usados % litros_por_lata)
numero_de_galoes = math.ceil(litros_faltantes / litros_por_galoes)
valor_de_galoes = numero_de_galoes * valor_do_galoes
print (f'e {numero_de_galoes} latas de 3.6 litros no total de R$ {valor_de_galoes}')
print (f'No total de R$ {valor_de_latas+valor_de_galoes} !')
