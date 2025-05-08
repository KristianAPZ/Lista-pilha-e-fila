def decimal_para_binario(decimal):
    pilha = []
    while decimal > 0:
        restante = decimal % 2
        pilha.append(restante)
        decimal = decimal // 2

    binario = []

    for i in range(len(pilha)):
        binario.append(str(pilha.pop()))

    print("".join(binario))


decimal_para_binario(10)
