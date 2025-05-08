class Impresora:
    def __init__(self):
        self.fila = []

    def adicionar(self, nomeDocumento, paginas):
        self.fila.append({"nome": nomeDocumento, "paginas": paginas})
        print(f"Documento {nomeDocumento} foi adicionado à fila.")

    def imprimir(self):
        if not self.fila:
            print("\nNão tem documentos na fila.")
        else:
            documento = self.fila.pop(0)
            print(
                f"\nImprimindo {documento['nome']} com {documento['paginas']} páginas.")

    def ver_fila(self):
        if not self.fila:
            print("\nNão tem documentos na fila.")
        else:
            print("\nDocumentos na fila:")
            for documento in self.fila:
                print(f"{documento['nome']} - {documento['paginas']} páginas.")


impresora = Impresora()
impresora.adicionar("Relatório", 10)
impresora.adicionar("Apresentação", 5)

impresora.ver_fila()

impresora.imprimir()
impresora.imprimir()
impresora.imprimir()
