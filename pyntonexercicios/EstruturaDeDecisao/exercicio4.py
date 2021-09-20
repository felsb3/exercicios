# Estrutura De Decisão exercício 4 https://wiki.python.org.br/EstruturaDeDecisao
# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

entrada = str(input('Inserir uma letra: ')).upper()
if entrada == 'A' or entrada == 'E' or entrada == 'I' or entrada == 'O' or entrada == 'U':
    print('A letra digitada é vogal.')
else:
    print('A l1etra digitada é consoante.')
