# valor = ml
# Valor por litro = 1000 ml / g
# Valor por litro * ml = valor " 1000
# Valor = valor " 1000 / ml

ml = float(input('Digite os ml: '))
valor = float(input('Digite o valor em R$: '))
valor_por_litro = (valor * 1000) / ml
print(f"O valor por litro é R$ {round((valor_por_litro), 2)}.")
