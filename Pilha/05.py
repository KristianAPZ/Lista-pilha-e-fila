def avaliar_posfixa(expressao):
    pilha = []
    operacoes = expressao.split()

    for operacao in operacoes:
        if operacao in '*+-/':
            a = pilha.pop()
            b = pilha.pop()

            if operacao == '*':
                pilha.append(a * b)
            elif operacao == '+':
                pilha.append(a + b)
            elif operacao == '-':
                pilha.append(a - b)
            elif operacao == '/':
                pilha.append(a / b)
        else:
            pilha.append(float(operacao))

    print(pilha.pop())


avaliar_posfixa("2 3 +")
