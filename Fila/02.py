def palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()

    pilha = []
    fila = []

    for letra in palavra:
        pilha.append(letra)
        fila.append(letra)

    while len(pilha) > 0:
        pilha_letra = pilha.pop()
        fila_letra = fila.pop(0)
        if pilha_letra != fila_letra:
            return False
    return True


print(palindromo("Ovo"))
print(palindromo("Reconocer"))
print(palindromo("Hola"))
