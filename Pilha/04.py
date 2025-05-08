class EditorDeTexto:
    def __init__(self):
        self.pilha = []
        self.conteudo = ""

    def adicionar(self, texto):
        self.pilha.append(texto)
        self.conteudo += texto
        print(f"\nFoi adicionado: {texto}")

    def desfazer(self):
        if len(self.pilha) == 0:
            return ("Nada para desfazer")

        ultima_acao = self.pilha.pop()
        tamanho = len(ultima_acao)

        self.conteudo = self.conteudo[:-tamanho]

        return f"Foi desfeito: {ultima_acao}\n"

    def mostrar_texto(self):
        return self.conteudo


editor = EditorDeTexto()

editor.adicionar("Kristian hola ")
editor.adicionar("como estás ")
editor.adicionar("todo bien?")

print(editor.mostrar_texto())

print(editor.desfazer())
print(editor.mostrar_texto())

editor.adicionar("muy mal")
print(editor.mostrar_texto())
