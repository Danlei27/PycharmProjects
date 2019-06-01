dia=input('dia')
mes=input('mes')
ano=input('ano')
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Você nasceu no dia' ,cores ['azul'],dia, 'do' ,mes, 'de' ,ano,cores['limpa'], '.correto?')
