# PROJETO VIAJEM
#DAS CIDADES A BAIXO PRA QUAIS CIDADES GOSTARIA DE VIAJAR?
#LISTA DE CIDADES
#QUAL VALOR DISPONIVEL PARA VIAJEM?
#COM O VALOR DISPONIVEL PODE VISISTAR PRA TAL CIDADE
#iniciando projeto com listas
diarias=[350,300,250,200]
cidades=['FORTALEZA', 'FLORIANOPOLIS', 'SÃO PAULO', 'MATO GROSSO DO SUL']
print('Olá! Bem vindo (a) a sua agência de viagens!')
n= int(input(''' Escolha um dos destinos a baixo:
[0] FORTALEZA
[1] FLORIANOPOIS
[2] SÃO PAULO
[3] MATO GROSSO DO SUL ?: '''))
cidades.append(n)
dias=int(input('Quantos dias de viagem?: '))
valor= dias* diarias[n]
cidades=cidades[n]
print('A viagem para {} irá sair R${:.2f}'.format(cidades,valor))
