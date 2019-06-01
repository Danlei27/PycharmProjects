# crie um programa que gerencie o aproveitamento de um jogador
#de futebeol. O programa vai ler o nome do jogador e quantas
#partidas ele jogou.Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos
#durante o campeonato
jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(0,partidas):
    gols.append(int(input(f'Quantos gols na partida {p}?')))
    total += gols[p]
jogador['gols'] = gols
jogador['total'] = total
print(f'{28*"=-"}\n{jogador}\n{28*"=-"}')
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print(f'{28*"=-"}\nO jogador {jogador["nome"]} jogou {partidas} partidas.')
for p, g in enumerate(gols):
    print(f'    => Na partida {p}, fez {g} gols.')
print(f'Foi um total {jogador["total"]} gols')