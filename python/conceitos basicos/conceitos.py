#o python é uma linguagem orientada a objeto

#Primeiros passos, definição de variáveis
profissao = str("Engenheira de analytics") #String
idade = 20 #Inteiro
peso = 50.0 #float
inteligente = True #Booleano

# Operadores Aritméticos: (+, -, *, /, // (divisão inteira), % módulo, ** (exponenciação) )
# Operadores para comparação: ==, !=, >, <, >=, <=
# Operadores Lógicos: and, or, not
# Atribuição: =, +=, -=, *=, /=

#Estrutura de decisão no python
if idade < 20:
    print("Sou menor de idade")
elif idade == 20:
   print("Entrei na vida adulta agora")
else:
   print("Já sou maior de idade")


#For é usado para percorrer algo, quando eu sei o limite
#range(inicio, fim (nunca pega o último valor), intervalo)
for i in range(0, 2):
    print(i)

for c in range(10, 0, -2): # aqui ele está contando ao contrário pulando de dois em dois
    print(c)

#Usando input
n = int(input("Digite um número:"))

#Usando o for para ler diversos números e trazer a soma entre eles
contador = 0

for vc in range(1, 1):
    n = int(input("Digite um numero"))
    contador += n
print(contador)

#While
c = 1
while c < 2:
    print(c)
    c += 1
print('fim')

#O while serve para quando eu não sei o limite, ou seja, "enquanto não chegar até algo faça"
# ponto de parada, enquanto for diferente de zero ele executa

r = 'S'
while r == 'S':
    n = int(input('Digite um valor por preferência'))
    r = str(input("Quer continuar? [S/N]")).upper()
print('Fim')


#Funções é utilizado def para definir uma função
def dizerOi(nome):
    print(f'olá {nome}, engenheira de dados linda')

# chamando a função
dizerOi('Rayane')

#Listas
listaCertificados = [1, 2, 3, 4]
listaCertificados.append(5) #Adicionando elementos a lista
listaCertificados[0] = 10 #substituindo
listaCertificados.remove(listaCertificados[2])

#Fatiamento
sublista = listaCertificados[1:4] # pega os elementos do indice 1 até o indice 3
print(sublista)

#Dicionário ele armazena pares de chave e valor
dicionario = {'Nome': "Rayane",
              'Idade' : '20'
              }

dicionario['cidade'] = 'são paulo' # adicionando nova coluna com valor

#instalação de bibliotecas: Use pip para instalar bibliotecas externas
# pip install numpy















