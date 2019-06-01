#nome = input('Qual é seu nome?')
#if nome == 'Danlei':
#    print('Que nome lindo!')
#condição simples-------------------------------------------
#else:
#   print('Seu nome é bem normal.')
#print('Tenha um bom dia, {}!.'.format(nome))
#Estrutura condicional composta------------------------------

nome = input('Qual é seu nome?')
if nome == 'Danlei':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jèssica Juliana ':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem comum.')
print('Tenha um bom dia, {}!'.format(nome))
#estrutura  condicionada aninhada-----------------------------