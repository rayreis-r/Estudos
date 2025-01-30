from  time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print("""
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] Sair do programa
    """)
    opcao = int(input("Qual é a sua opção?"))

    if opcao == 1:
        print("A soma dos numeros {} e {} é: {}".format(v1, v2, v1 + v2))
    elif opcao == 2:
        print("A multiplicacao dos numeros {} e {} é: {}".format(v1, v2, v1 * v2))
    elif opcao == 3:
        maior = v1
        if v1 < v2:
            maior = v2
        print("Entre {} e {} o maior valor é {}".format(v1, v2,maior))
    elif opcao == 4:
        print("Informe os números novamente")
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    else:
        print("Finalizando")
        sleep(2)

print('Fim do programa')