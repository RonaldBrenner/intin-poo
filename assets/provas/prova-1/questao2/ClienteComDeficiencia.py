from Cliente import Cliente

class ClienteComDeficiencia(Cliente):
    def __init__(self, nome, idade):
        Cliente.__init__(self, nome, idade)

    def calcular_valor_final_passagem(self, valor):
        return 0
