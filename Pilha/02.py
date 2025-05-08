def verifica_balanceamento(expressao):
    pilha = []
    inicio = "{(["
    final = "})]"
    for char in expressao:
        if char in inicio:
            pilha.append(char)
        elif char in final:
            if not pilha:
                return False

            top = pilha.pop()

            if inicio.index(top) != final.index(char):
                return False

    print(len(pilha) == 0)


verifica_balanceamento("{[()]}")
