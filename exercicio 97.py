# Faça um programa que tenha uma função chamada
#escreva(), que reba um texto qualquer como parâmetro e,
#mostre uma mensagem com tamanho adaptável.
#ex:
#escreva('Olá, mundo!')
#saida:
#''''''''''''''''''
#Olá, mundo!
#''''''''''''''''''
def escreva(msg):
    print(f'{(len(msg) + 4) * "-"}\n  {msg}\n{(len(msg) + 4) * "-"}')


escreva('Olá mundo')
escreva('CURSO EM VIDEO NO YOUTUBE')
escreva('CeV')