# Exercicios Funcoes exercício 1 https://wiki.python.org.br/ExerciciosFuncoes?highlight=%28%28ExerciciosFuncoes%29%29
# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n

def imprimir_triangulo_de_numeros(n: int):
    for i in range(1, n + 1):
        for _ in range(i):
            print(i, end='   ')
        print('')


print('Triangolo com 1')
imprimir_triangulo_de_numeros(1)

print('Triangolo com 2')
imprimir_triangulo_de_numeros(2)

print('Triangolo com 3')
imprimir_triangulo_de_numeros(3)

print('Triangolo com 7')
imprimir_triangulo_de_numeros(7)
