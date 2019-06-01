#Faça um Programa que mostre a tabuada de vàrios Números,
# um de cada vez, para cada valor digitado pelo Usuário
#O programa será interrompido quando o Número solicitado for negativo.
while True:
  n = int(input('Degite o nùmero da tabuada desejada: '))
  if n < 0 :
      break
  t = 0
  while t != 10:
       t += 1
       print(f'{n} x {t} = {n*t} ')
print('PROGRAMA TABUADA ENCERRADO .Volte sempre!')

