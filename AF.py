class AF:

    def __init__(self):
        self.estados = []
        self.estado_inicial = None

    def add_estado(self, estado):
        self.estados.append(estado)

    def add_estado_inicial(self, estado):
        self.estado_inicial = estado
        self.add_estado(estado)