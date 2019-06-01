#Crie um programa que tenha uma função chama voto()
#que vai receber como parametro o ano de nascimento de uma pessoa
#retornando um valor literal indicado se uma pessoa tem voto NEGADO, OPCIONAL OU
#OBRIGATÓRIO nas eleiçôes.
def voto(ano):
    from datetime import date
    i = date.today().year - ano
    print(f'com {i} anos: ', end='')
    if i <= 15 :
        return ' NÃO VOTA! '
    elif 18 > i > 15 or i > 65:
        return 'VOTO OPCIONAL!'
    else:
        return 'VOTO OBRIGATÓRIO!'


ano = int(input('Em que  ano você  nasceu? '))
print(voto(ano))