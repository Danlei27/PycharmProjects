print('\033[31mOlá mundo!')
print('\033[31;43mOlá mundo!')
print('\033[1;31;43mOlá mundo!')
print('\033[1;31;43mOlá mundo!\033[m')

print('\033[4;30;45mOlá mundo!\033[m')
print('\033[30;mOlá mundo!\033[m')
print('\033[37mOlá mundo!\033[m')
print('\033[0;33;44mOlá mundo!\033[m')
print('\033[7;33;44mOlá mundo!\033[m')
print('\033[7;30mOlá mundo!\033[m')

a = 7
b = 8
print('Os valores são \033[33m{}\033[m e \033[31m{}\033[m'.format(a,b))
print('Os valores são \033[44m{}\033[m e \033[33;45m{}\033[m'.format(a,b))
nome = 'Danlei Santos'
print('Olá! munito prazer em ti conhecer, {}{}{}.'.format('\033[4;33m' ,nome, '\033[m'))
cores = {'limpa': '\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30m'}
print('Olá! muito prazer em ti conhecer,{}{}{}'.format(cores['azul'] ,nome, cores['limpa']))