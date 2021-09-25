# Estrutura De Decisão exercício 3 https://wiki.python.org.br/EstruturaDeDecisao
# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

entrada = str(input('favor digitar F para feminino e M para masculino: ')).upper()
if entrada == 'F':
    print('o sexo inormado foi Feminnido')
elif entrada == 'M':
    print('o sexo inormado foi Masculino')
else:
    print('Neste caso o sexo ficou Inválido.')

sexo = input('Digite "F" para feminino, "M" para masculino e "I" para não declarar: ').upper()
print (sexo)
if sexo == 'M':
  print ('Masculino')
elif sexo == 'F':
  print ('Feminino')
elif sexo == 'I':
  print ('Indefinido')
else:
  print ('Indefinido')
