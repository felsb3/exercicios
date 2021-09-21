# Estrutura De Decisão exercício 20 https://wiki.python.org.br/EstruturaDeDecisao
# Faça um Programa para leitura de três notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota_1 = float( input ('incira sua nota do primeiro bimestre: '))
nota_2 = float( input ('incira sua nota do segundo bimestre: '))
nota_3 = float( input ('incira sua nota do terceiro bimestre: '))
nota_4 = float( input ('incira sua nota do quarto bimestre: '))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
if media >= 9:
  print ('Parabens passou com excelencia')
elif media >= 7:
  print ('Você passou')
else:
  print ('Você não está aprovado')
print (f'Sua média é: {media}')
