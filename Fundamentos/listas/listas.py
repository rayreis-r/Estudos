# Lista é uma estrutura de coleções de dados mutaveis e que permitem guardar multiplos valores em uma unica variavel
# Ela pode ser mudada ao longo do tempo e pode misturar tipos de dados em uma unica lista

print('################## SOBRE LISTAS ##################')
lista_compras = ['Banana', 'Maça', 'Shampoo', 'Creme de Pentear']
print(lista_compras)

print('################## Acessando os Elementos ##################')
# Acessando os elementos - para acessar usamos a indexação que é contadaa a partir do 0 usamos o [] para acessar o indice de uma lista

print('Primeiro item da lista de compras:', lista_compras[0]) #Pegando o primeiro item da lista de compras
print('Ultimo item da lista de compras:', lista_compras[-1]) #Pegando o ultimo item da lista de compras 
print('Penultimo item da lista de compras:', lista_compras[-2]) #Pegando o peultimo item da lista de compras 

print('################## Fatiamento (Slicing) ##################')

# Fatiamento (Slicing) - pegamos uma pequena parte da lista no formato lista[inicio:fim:passo] o indice final não é incluido
print('Indice do 1 ao 3', lista_compras[1:4]) # Ultimo indice nunca é incluso 
print('Do inicio até o indice 2', lista_compras[:3]) 
print('Do indice 1 até o fim', lista_compras[1:])
print('Do inicio até o fim pulando de 2 em 2', lista_compras[::2]) 


print('################## Trocando os valores da lista  ##################')

lista_compras[1] = 'Sabonete' # O segundo item da lista será sabonete
print('Lista Modificada:', lista_compras)

print('################## Principais métodos de lista  ##################')

# append('valor') > Adiciona um item ao final da lista
# insert (posição, valor) > Adiciona um item na posição especificada
# extend(iterable) > Adiciona todos os elementos de outra lista/coleção ao final

lista_compras.append('Chocolate') # Adicionando choclate ao final da lista
print('Lista Modificada:', lista_compras)

lista_compras.insert(0, 'Refrigerante') # Adicionando Refrigerante no começo da lista
print('Lista Modificada:', lista_compras)

lista_compras.extend(['uva', 'morango', 'maracuja']) # Adicionando frutas em conjunto a lista

print('################## Removendo elementos da lista  ##################')

# pop(index) : Remove e retorna o item na posição informada
# remove(valor) : Remove a primeiro valor informado que for encontrado
# clear() : Esvazia a lista inteira

lista_compras.pop(1)
print('Lista Modificada:', lista_compras)

lista_compras.remove('Chocolate')
print('Lista Modificada:', lista_compras)

lista_compras.clear()
print('Lista Modificada:', lista_compras)


# Operações uteis 
# len(lista): Retorna a quantidade de elementos.
# count(val): Conta quantas vezes um valor aparece.
