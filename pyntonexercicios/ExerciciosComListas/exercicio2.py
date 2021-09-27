# Exercícios Com Listas exercício 2 https://wiki.python.org.br/ExerciciosListas
# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
lista = []
for _ in range(10):
    numero = float(input('Digite um número: '))
    lista.append(numero)

lista.reverse()
print(lista)
