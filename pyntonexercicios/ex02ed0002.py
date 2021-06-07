# Estrutura de Decisão exercício 2 Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = input('Digite aqui seu sexo "M" para masculino "F" para feminino e "I" para não definir: ').upper()
if sexo == 'M':
    print('Masculino')
elif sexo == "F":
    print('Feminino')
elif sexo == "I":
    print('Indefinido')
else:
    print('sexo invalido')
print('Finalizou o programa')
