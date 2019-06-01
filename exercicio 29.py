#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

m=float(input('Leitor de velocidade'))
if m > 80:
    print('\033[31m''Você foi multado!''\033[m' ' excedeu a 80Km/h!\nSua multa é de {:.2f}R$'.format((m-80)*7))
print('\033[32m''Boa viagem dirija com segurança.')