#crie um programa que leia nome, ano de nascimento e
#carteira de trabalho e cadastre-os (com idade) em um dicionário
#se pos acaso o ctps for diferente de Zero, o dicionário receberá
#tambem o ano de contratação e o salário.calcule e acrescenta, além
#da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
data = date.today().year
dados = {}
dados['nome'] = str(input('Nome: '))
nasci = int(input('Ano de  nascimento: '))
dados['idade'] = data - nasci
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário : R$'))
    dados['aposentadoria']= (dados['contratação'] + 35)  - nasci
print(30*'=-')
for k, v in dados.items():
    print(f'{k} tem o valor de {v}')