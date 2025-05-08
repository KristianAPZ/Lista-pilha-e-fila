def inverter_string(texto):
    pilha = []
    invertida = []
    for char in texto:
        pilha.append(char)

    while pilha:
        invertida.append(pilha.pop())

    print("".join(invertida))


inverter_string("Python")
inverter_string("Hola mundo")
