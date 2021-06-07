import math
# while area_a_ser_pintada > 200:
area_a_ser_pintada = int(input('digite a área, em metros quadrados a ser pintada: '))  # area em metros quadrados
# print (area_a_ser_pintada)
# area_a_ser_pintada += 1
area_com_folga = area_a_ser_pintada * 1.1
metros_por_litro = 6
litros_a_serem_usados = area_com_folga / metros_por_litro
litros_por_lata = 18
numero_de_latas = math.ceil(litros_a_serem_usados / litros_por_lata)
valor_com_apenas_latas = numero_de_latas * 80
print(f'Você deverá usar {numero_de_latas} latas de 18 litros, no valor de R$ {valor_com_apenas_latas}')

litros_por_galao = 3.6
nunero_de_galoes = math.ceil(litros_a_serem_usados / litros_por_galao)
valor_com_apenas_galoes = nunero_de_galoes * 25
print(f'Você deverá usar {nunero_de_galoes} galões de 3.6 litros no valor de R$ {valor_com_apenas_galoes}')

# compra de tintas otimiada por valor
numero_de_latas_otimizado = math.floor(litros_a_serem_usados / litros_por_lata)
valor_de_latas_otimizado = numero_de_latas_otimizado * 80
litros_faltantes = litros_a_serem_usados % litros_por_lata
nunero_de_galoes_otimizado = math.ceil(litros_faltantes / litros_por_galao)
valor_com_galoes_otimizado = nunero_de_galoes * 25

valor_total = valor_de_latas_otimizado + valor_com_galoes_otimizado

print(f'Você deverá usar {numero_de_latas_otimizado} latas de 18 litros {nunero_de_galoes_otimizado}'
      f' galões de 3.6 litros, no valor de R$ {valor_total}')
print('####################################################################')
if valor_com_apenas_latas < valor_com_apenas_galoes and valor_com_apenas_latas <= valor_total:
    print(f'Você deverá usar {numero_de_latas} latas de 18 litros, no valor de R$ {valor_com_apenas_latas}')

if valor_com_apenas_galoes <= valor_total and valor_com_apenas_galoes < valor_com_apenas_latas:
    print(f'Você deverá usar {nunero_de_galoes} galões de 3.6 litros no valor de R$ {valor_com_apenas_galoes}')

if valor_total < valor_com_apenas_galoes and valor_total < valor_com_apenas_latas:
    print(f'Você deverá usar {numero_de_latas} latas de 18 litros {nunero_de_galoes}'
          f' galões de 3.6 litros, no valor de R$ {valor_total}')

print('############### compra de tintas otimizada por valor ###############')
