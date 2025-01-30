s = str(input("Digite seu sexo")).upper()

while s not in 'MmFf':
    s = str(input("Digite seu sexo")).upper()
print('Seu sexo é: {}'.format(s))