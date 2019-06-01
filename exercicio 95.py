#Aprimore o desafio 093 para qie ele funcione com vários jogadores, incluindo um sistema de visualiçao
#de detalhes do aproveitamemnte de cada jogador.
jogador = dict()
gols = list()
jogadores = list()
resp = 'S'
while resp == 'S':
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(0,partidas):
        gols.append(int(input(f'   Quantos gols na partida {p+1}?')))
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols.copy())
    jogadores.append(jogador.copy())
    gols.clear()
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
print(f'{25*"=-"}\n{"cod nome":<20}{"gols":<20}{"total":<15}\n{25*"--"}')
for n, j in enumerate(jogadores):
  print('{:<20}{:<20}{:<15}'.format(f'  {n} {j["nome"]}',f'{j["gols"]}',f'{j["total"]}'))
while True:
    cod = int(input(f'{25*"--"}\nMostrar dados de qual jogador? (999 para parar)'))
    while 999 != cod > len(jogadores) - 1 :
      print(f'ERRO! não existe jogador com código {cod}!')
      cod = int(input(f'{25 * "--"}\nMostrar dados de qual jogador? (999 para parar)'))
    if cod == 999:
        break
    print(F'--LEVANTAMENTO DO JOGADOR {jogadores[cod]["nome"]}:')
    for j, g in enumerate(jogadores[cod]['gols']):
        print(f'   No jogo {j + 1} fez {g} gols.')
print('<< VOLTE SEMPRE >>')