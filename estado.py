class Estado:

    def __init__(self, nombre):
        self.nombre = nombre
        self.transiciones = []
        self.aceptacion = False
        
    def add_transicion(self, transiciones): # transiciones -> [parametro, estado_objetivo]
        self.transiciones.append(transiciones)

    def set_aceptacion(self, aceptacion):
        self.aceptacion = aceptacion
