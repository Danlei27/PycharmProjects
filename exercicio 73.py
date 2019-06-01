#crie um tupla preenchida com os 20 primeros colocados da tabela dp
#campeonato brasileiro de futebol, na ordem de colocação.Depois mostras:
#a) Apenas os 5 Primeiros colocados
#b) Os últimos 4 colocados da tabela
#c) Umas lista coms os times em ordem alfabética.
#d) Em que poição na tabela está o time da chapecoense.
times =('PALMEIRAS',   'FLAMENGO',  'INTERNACIONAL',  'GRÊMIO', 'SÃO PAULO','ATLÉTICO-MG',  'ATHLETICO',  'CRUZEIRO',  'BOTAFOGO',  'SANTOS',  'BAHIA','FLUMINENSE',  'CORINTHIANS',   'CHAPECOENSE', 'CEARÁ', 'VASCO',  'SPORT','AMÉRICA-MG',  'VITÓRIA',  'PARANÁ')
todos = f'Lista do times do Brasileirão: {times}'
primeiros = f'Os 5 primeiros colocados: {times[:5]}'
ultimos = f'Os 4 ultimos colocados: {times[-4:]}'
alfa = f'Os time em ordem alfabetica:  {sorted(times)}'
time = 'O time da Chapecoense está na {} ª posição'.format(1+times.index('CHAPECOENSE'))
efeito = 10*'\033[33m-=-\033[m'
config = (efeito, todos, efeito, primeiros, efeito, ultimos, efeito, alfa, efeito, time)
for c in config:
    print(c)
# Ou
#for pos, c in enumerate(times):
 #   if c == 'CHAPECOENSE':
  #   print(f'O time da {c} está na {pos}ª posição')
