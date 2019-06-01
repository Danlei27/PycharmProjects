# Escreva um programa que leia um nùmero n inteiro
# qualquer e mostre na tela os n primeiros elementos
#   de uma sequência de fibonacci.
#Ex:

#0→1→1→2→3→5→8 , 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584.
n1 = 1
n2 = 0
cont = int (input('Sequência de Fibonacci\nQuantos termos gostaria de ler? '))
while  not cont == 0  :
    cont += -1
    print(n2, end=' → ')
    n2 = n2 + n1
    while  cont % 2 != 0:
        cont += -1
        print(n1, end=' → ')
        n1 = n1 + n2
print('Fim')
# segundo modo --------
t1 = 0
t2 = 1
n = int(input('Quantos temos você que ler?'))
cont = 3
print('{} → {}'.format(t1,t2),end='')
t3 = t1 + t2
while  cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' Fim')








