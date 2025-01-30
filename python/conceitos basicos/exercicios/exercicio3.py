contador = 0
soma = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        contador += 1
print("A soma de todos os {} valores solicitados é: {}".format(contador, soma))