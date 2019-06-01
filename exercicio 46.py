# faça um programa que mostre na tela uma
#  contagem regressiva para o estouro de
#  fogos de artificio, indo de 10 até 0,
#  com uma pausa de 1 segundo entre eles.
from time import sleep
print('\033[32mVai começar a queima  dos fogos de artificios em..\033[m')
sleep(1)
for c in range(10, -1, -1 ):
    sleep(1)
    print(c)
print('\033[34m'' CABUM! ''\033[36m''BUM ''\033[35m''BAM! ')


