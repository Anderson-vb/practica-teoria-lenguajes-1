class Transicion:

    def __init__(self, parametro, estado_objetivo):
        self.parametro = parametro
        self.estado_objetivo = estado_objetivo

    def get_parametro(self):
        return self.parametro

    def get_estado_objetivo(self):
        return self.estado_objetivo