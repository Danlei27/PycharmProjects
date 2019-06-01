# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário.No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
from random import randint
dados = [[],[],[],[]]
for j in range(0,4):
    dado = randint(1,6)
    dados[j].append(dado)
    dados[j].append(j+1)
    print(f'Jogador{j+1} tirou {dado} no dado.')
dados.sort(reverse=True)
print(20*'-=','\n == RANKING DOS JOGADORES ==')
for c in range(0,4):
  print(f'  {c+1}º lugar: jogador{dados[c][1]} com {dados[c][0]}')

#modo 2===================================================================
from random import randint
dados = []
lista = []
for j in  range(1,5):
 dados.append(randint(1,6))
 lista.append(f'j{j}')
 lista.append(dados[j-1])
dados.sort(reverse=True)

for c in range(0,4):
  print(f'{lista[lista.index(dados[0])-1]} jogou {dados[0]}')
  del lista[lista.index(dados[0])-1]
  del lista[lista.index(dados[0])]
  del dados[0]
#modo 3=====================================================================
from random import randint
joga = {}
ordem = []
for j in range(1, 5):
    dado = randint(1, 6)
    joga[f'Jogador{j}'] = dado
    print(f'Jogador{j} tirou  {dado} no dado.')
for c in joga.items():
    ordem.append(c[::-1])
ordem.sort(reverse=True)
for p, d in enumerate(ordem):
    print(f'  {p+1}º lugar: {d[1]} com {d[0]}')
#modo 4 ==============================================
from random import randint
joga = {}
rank = []
for j in range(1, 5):
    joga[f'Jogador{j}'] =  randint(1, 6),f'Jogador{j}'
    print('{} tirou  {} no dado'.format(f'Jogador{j}',joga[f'Jogador{j}'][0]))
    rank.append(joga[f'Jogador{j}'])
rank.sort(reverse=True)
for p,d in enumerate(rank) :
    print(f'  {p+1} º lugar: {d[1]} tirou {d[0]} no dado.')

