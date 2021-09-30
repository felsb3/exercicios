import math

import mach as mach

palavra = str(input('Digite uma palavra: ').upper())

print('Jogo da Forca')
print('Descubra a palavra')

print('apalavra é:', end='')
for letra in palavra:
    print('_ ', end='')

conjunto_letras_palavra = set(palavra)
conjunto_letras_digitadas = set()
erros = 0
print()
quantidade_de_erros_possiveis = math.floor(len(palavra) * 0.6)
print(quantidade_de_erros_possiveis)

while (not conjunto_letras_palavra.issubset(conjunto_letras_digitadas)) and erros < quantidade_de_erros_possiveis:
    print()
    print()
    letra_digitada = input('Digite uma letra: ').upper()
    conjunto_letras_digitadas.add(letra_digitada)
    if letra_digitada in conjunto_letras_palavra:
        print('A palavra é: ', end='')
        for letra in palavra:
            if letra in conjunto_letras_digitadas:
                print(f'{letra} ', end='')
            else:
                print('_ ', end='')
    else:
        erros += 1
        print(f'-> Erro {erros} de {quantidade_de_erros_possiveis}. Tente novo!')

    print()
    print('Letras já digitadas', conjunto_letras_digitadas)

if erros < quantidade_de_erros_possiveis:
    print('Parabens, você ganhou!')
else:
    print('Infelizmente você perdeu!')
