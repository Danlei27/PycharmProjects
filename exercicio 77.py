#crie um progrma que tenha uma tupla com várias
#palavras (não usar acentos).depois disso, você
#deve mostras, para cada palavra, quais são as suas vogais.
palavras = ('CARRO', 'MOTO' , 'BICICLETA', 'HELICÓPTERO','AVIAO','CAVALO','CARROÇA','JATO','ESPAÇONAVE',)
vogais = 'AEIOU'
for p in range(0, len(palavras)):
  print(f'\nNa palavra {palavras[p]} temos', end=' ')
  for v in range(0, len(vogais)):
     print((palavras[p].count(vogais[v])*f'{vogais[v].lower():<2}' ),end='')
#segundo modo--------------------------------------------------------------------------------------------
palavras = ('CARRO', 'MOTO' , 'BICICLETA', 'HELICÓPTERO','AVIAO','CAVALO','CARROÇA','JATO','ESPAÇONAVE',)
for p in palavras:
    print(f'\nNa palavra {p} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
          print(letra.lower(),end=' ')
