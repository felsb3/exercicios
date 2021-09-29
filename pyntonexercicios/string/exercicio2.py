nome = input('Digite uma string: ').upper()

nome_intertido_por_letras = ''.join(reversed(nome))

nome_intertido_por_palavras = ' '.join(reversed(nome.split()))

print(f'Nome com letras em maiúsculo: {nome}')
print(f'Nome com letras em maiúsculo invertido por letras: {nome_intertido_por_letras}')
print(f'Nome com letras em maiúsculo invertido por palavras: {nome_intertido_por_palavras}')
