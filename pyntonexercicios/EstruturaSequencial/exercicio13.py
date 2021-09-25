# Estrutura Sequencial exercício 13 https://wiki.python.org.br/EstruturaSequencial
# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule
# seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7
#
# h = float(input('Favor informar sua altura em metros: '))
# sexo = str(input('Digite aqui seu sexo "M" para masculino "F" para feminino: ')).upper()
# if sexo == 'M':
#     peso_ideal = (72.7*h)-58
#     print(f' Para sexo Masculino seu peso ideal seria {peso_ideal} kg')
# elif sexo == "F":
#     peso_ideal = (62.1*h)-44.7
#     print(f'Para sexo Feminino seu peso ideal seria {peso_ideal} kg')
# else:
#     print('sexo invalido')
# print('Finalizou o programa')


while True:
    try:
        h = float(input('Favor informar sua altura em metros: '))
        sexo = str(input('Digite aqui seu sexo "M" para masculino "F" para feminino: ')).upper()
    except: ValueError:\
        print('Erro ')
    else:
        if sexo == 'M':
            peso_ideal = (72.7 * h) - 58
            print(f' Para sexo Masculino seu peso ideal seria {peso_ideal} kg')
            break
        elif sexo == "F":
            peso_ideal = (62.1 * h) - 44.7
            print(f'Para sexo Feminino seu peso ideal seria {peso_ideal} kg')
            break
        else:
            print('sexo invalido')
print('Finalizou o programa')
