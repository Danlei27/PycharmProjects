# faça um progrma que tenha uma função chama área()
# que receba as dimensões de um terreno retangular(largura e comprimento
# mostre a área do terreno.
def area(larg, comp):
    r = larg * comp
    print(f'A aréa de um terreno {larg}x{comp} é de {r}m².')


larg = float(input(f' Controle de terrenos\n{11 * "--"}\nLargura (m):'))
comp = float(input('Comprimento (m): '))
area(larg, comp)
