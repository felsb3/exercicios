# Exercicios Funcoes exercício 2 https://wiki.python.org.br/ExerciciosFuncoes?highlight=%28%28ExerciciosFuncoes%29%29
# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def imprimir_triangulo_de_numeros_crescente(n: int):
    for linha in range(1, n + 1):
        for coluna in range(1, linha + 1):
            print(coluna, end='   ')
        print('')


print('Triangolo com 1')
imprimir_triangulo_de_numeros_crescente(1)

print('Triangolo com 2')
imprimir_triangulo_de_numeros_crescente(2)

print('Triangolo com 3')
imprimir_triangulo_de_numeros_crescente(3)

print('Triangolo com 7')
imprimir_triangulo_de_numeros_crescente(7)
