import heapq


class FilaDePrioridade:
    def __init__(self):
        self.fila = []

    def adicionar(self, tarefa, prioridade):
        heapq.heappush(self.fila, (prioridade, tarefa))

    def remover(self):
        if not self.fila:
            return "Fila vazia"
        return heapq.heappop(self.fila)[-1]

    def ver_fila(self):
        if not self.fila:
            return "Fila vazia"
        return self.fila


fila = FilaDePrioridade()
fila.adicionar("Lista Calculo", 2)
fila.adicionar("Estudar prova", 1)
fila.adicionar("Lista python", 0)

print(fila.ver_fila())
fila.remover()
print(fila.ver_fila())
fila.remover()
print(fila.ver_fila())
fila.remover()
print(fila.ver_fila())
