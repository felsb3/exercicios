# Estrutura de Repetição exercício 12 Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
# inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.

tabuada = int(input('Tabuada de: '))
for i in range(1, 11, 1):
    x = tabuada*i
    print(f'{tabuada} x {i} = {x}')
