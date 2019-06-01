# faça um progrma que tenha uma função chamada ficha(), que receba
# dois parâmetros opcionais:o nome de um jogador e quantos gols ele marcou.
# O progrma deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado
# corretamente.
def ficha(jogador, gols):
    jogador = 'Desconhecido' if jogador.strip() == '' else jogador
    gols = 0 if gols.isnumeric() != True else gols
    return print(f'O jogador {jogador} fez {gols} gols(s) no campeonato.')


ficha(jogador=str(input(f'{20 * "--"}\nNome do jogador: ')), gols=str(input('Números de gols: ')))


# segundo --------------------------------------------------------------------------------------
def ficha(jogador='<Desconhecido>', gols=0):
    return print(f'O jogador {jogador} fez {gols} gols(s) no campeonato.')


j = str(input(f'{20 * "--"}\nNome do jogador: '))
g = str(input('Números de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gols=g)
else:
    ficha(j, g)


# terceiro modo -------------------------------------------------------------------
def ficha(jogador = '<Desconhecido>', gols= 0):
    print(f'O jogador {jogador} fez {gols} gols(s) no campeonato.')



j=str(input(f'{20*"--"}\nNome do jogador: '))
g=str(input('Números de gols: '))
if  j.strip() != '' and g.isnumeric() :
    ficha(jogador = j,gols=g)
else:
    if  j.strip() != '' and len(g) == 0:
       ficha(jogador=j)
    elif g.isnumeric() and len(j) == 0:
        ficha(gols=g)
    else:
        ficha()