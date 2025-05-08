class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.inicio = 0
        self.fim = 0
        self.tamanho = 0

    def adicionar(self, elemento):
        if self.tamanho == self.capacidade:
            return "Fila cheia"
        self.fila[self.fim] = elemento
        self.fim = (self.fim + 1) % self.capacidade
        self.tamanho += 1

    def remover(self):
        if self.tamanho == 0:
            return "Fila vazia"
        elemento_removido = self.fila[self.inicio]
        self.fila[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1
        return elemento_removido


fila = FilaCircular(5)
try:
    fila.adicionar(1)
    fila.adicionar(2)
    fila.adicionar(3)
    fila.remover()
    print(fila.fila)
    fila.adicionar(4)
    fila.adicionar(5)
    fila.adicionar(6)
    print(fila.fila)
    print(fila.adicionar(7))
except Exception as e:
    print(f"Erro: {e}")
