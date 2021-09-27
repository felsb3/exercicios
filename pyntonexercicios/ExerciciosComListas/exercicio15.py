# Exercícios Com Listas exercício 15 https://wiki.python.org.br/ExerciciosListas
# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
# quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# 1 Mostre a quantidade de valores que foram lidos;
# 2 Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# 3 Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# 4 Calcule e mostre a soma dos valores;
# 5 Calcule e mostre a média dos valores;
# 6 Calcule e mostre a quantidade de valores acima da média calculada;
# 7 Calcule e mostre a quantidade de valores abaixo de sete;
# 8 Encerre o programa com uma mensagem;
notas = []

while True:
    entrada = input('Digite um número: ')
    if entrada == '-1':
        break
    notas.append(float(entrada))

tamanho = len(notas)
print(f'Foram lidas {tamanho} notas.')
print(' '.join([str(nota) for nota in notas]))
notas.reverse()

for nota in notas:
    print(nota)

soma = sum(notas)

print(f'A soma das notas é: {soma}')

media = soma / tamanho

print(f'A média das notas é: {media}')

print('Notas acima da média: ')

print(' '.join([str(nota) for nota in notas if nota > media]))

print('Notas abaixo de 7: ')

print(' '.join([str(nota) for nota in notas if nota < 7]))

print('Encerrando programa de estatística de notas!')
