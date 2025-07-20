#treinando python

# import uteis imporantando um módulo da pasta raiz
from uteis.funcoesPy.func import media
# importante seguir o caminho da estrutura de pasta certinho

#Variaveis
nome = str("Rayane")
namorado = True
mesesNamoro = 14
mensagem = str

#Condicionais
if namorado == True:
    namorado = 'Sim'
else:
    namorado = 'Não'

if mesesNamoro <= 5:
    mensagem = 'Namoro recente'
elif mesesNamoro > 5 and mesesNamoro <= 8:
    mensagem = 'Vocês estão firmes'
else:
    mensagem = 'Já podem se casar'


#INPUT
nome = str(input('Digite seu nome'))
possuiNamorado = str(input('Tem namorado(a)?'))


if possuiNamorado == 'sim' :
    mesesNamoro = int(input('Há quantos meses vocês estão juntos'))
    suaMensagem = str(input('Insira uma mensagem para ele'))
    possuiNamorado = 'possui'
    print(f'Olá {nome}, você {possuiNamorado} namorado, estão a {mesesNamoro} meses juntos e {mensagem}, '
          f'o seu recado para ele(a) é: {suaMensagem}')

else:
    'Não possui'
    print(f'Olá {nome}, você irá encontrar seu amor')


#Conferindo o tipo das variaveis
print(type(mesesNamoro))

#Listas : conjunto de dados
lista_frutas = ['Morango', 'uva', 'melancia']

#Declarando lista
valores=list(range(1,10))
print(valores)

#Adicionando
lista_frutas.append('Rayane') #Adicionando no final
lista_frutas.insert(0, 'banana') #Adicionando em qualquer posição

#Apagando elemento
del lista_frutas[1]
lista_frutas.pop(2)
lista_frutas.remove('uva') #Eliminando pelo conteudo

#Acessando
print(lista_frutas)

#Colocando os valores em ordem
valores.sort() #Altera em ordem crescente
valores.sort(reverse=True) #Altera para ordem decrescente
print(valores)

#Visualizando uma lista
print(len(valores))

#Estrutura de repetição

# for i in range(inicio, fim, intervalo):
for  i in range(5, 20, 2) :
    print(i + 1)



# Modularização: foco é dividir um programa grande
#Chamando a função que está na pasta uteis, para isso basta adicionar o import e chamar o modulo antes da função
media()

#Pacotes é uma pasta que contém os modulos como Controller, model, src e etc, em cada uteis eu posso ter varios modulos
#exceções é quando não há um erro de sintaxe mas há um erro na entrada de dados try: tente algo except: falhou

try:
    a = int(3)
    b = int(0)
    r = a/b
except Exception as erro:
    print('tivemos um problema, o problema encontrado foi', erro.__class__)
else:
    print('resultado', r)
finally: #vai acontecer sempre independente do erro ou não
    print('volte sempre')







