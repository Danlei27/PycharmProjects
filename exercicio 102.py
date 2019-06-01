# Crie um programa que tenha uma função fatorial()
# que receba dos parâmetros: o primeiro que indique o
# número a calcular e o outro chamado show, que será um valor lógico
# (opcional) indiando se será mostrado ou não na tela o processo de
# cálculo do fatorial.
def fatorial(num=0, show=False):
    """
    Calcular o fatorial de um número.
    :param num:O número a ser calculado.
    :param show:(Opcional) mostra ou não a conta.
    :return:O valor do fatorial de um número n.
    """
    print(18*f'{"--"}')
    if show == True:
        for c in range(num, 1, -1):
            print(c,end=' x ')
        print(f'1 = ',end='')
    f = 1
    for c in range(num, 1, -1):
        f *= c
    return f


print(fatorial(8, True))
help(fatorial)
#segundo=============================================================
def fatorial(num=0, show=False):
    """
        Calcular o fatorial de um número.
        :param num:O número a ser calculado.
        :param show:(Opcional) mostra ou não a conta.
        :return:O valor do fatorial de um número n.
        """
    print(18 * f'{"--"}')
    f =1
    for c in range(num, 1, -1):
        f *= c
        if show:
            print(c,end=' x ')
    if show:
        print(f'1 = ',end='')
    return f


print(fatorial(5, True))
help(fatorial)