# crie um programa que tenha a função leiaint(),
# que vai funcionar de forma semelhante à função
# input() do python, só que fazendo a validação para
# aceitar apenas um valor númerico.
# ex
# n = leiaint('digite um n')
def leiaint(msg):
    num = str(input(f'{15*"--"}\n{msg}')).strip()
    while not num.isnumeric():
          print('\033[31m''ERRO! Digite um número inteiro válido.\033[m')
          num = str(input(f'{msg}')).strip()
    return num


n = leiaint('Digite um número: ')
print(f'você acaba de digiar o nùmero {n}.')
