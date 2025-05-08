class FilaDeAtendimento:
    def __init__(self):
        self.fila = []

    def entrada_cliente(self, cliente):
        self.fila.append(cliente)
        print(f"Cliente {cliente} entrou na fila.")

    def atender_cliente(self):
        if not self.fila:
            print("Nenhum cliente na fila.")
            return None
        cliente = self.fila.pop(0)
        return f"Atendendo cliente {cliente}."

    def clientes(self):
        print("\nClientes na fila:")
        if not self.fila:
            print("Nenhum cliente na fila.")
            return None
        else:
            for i, cliente in enumerate(self.fila):
                print(f"{i + 1} - {cliente}")


FilaDeAtendimento = FilaDeAtendimento()
FilaDeAtendimento.entrada_cliente("Kristian")
FilaDeAtendimento.entrada_cliente("Leo")
FilaDeAtendimento.clientes()

FilaDeAtendimento.atender_cliente()
FilaDeAtendimento.clientes()

FilaDeAtendimento.atender_cliente()
FilaDeAtendimento.clientes()
