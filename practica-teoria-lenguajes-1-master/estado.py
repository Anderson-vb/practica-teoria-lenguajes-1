from operaciones import derivar
from transicion import Transicion

class Estado:

    def __init__(self, regex):
        self.regex = regex
        self.transiciones = []
        self.nombre = ''

    def add_transicion(self, caracter, estado):
        transicion = Transicion(caracter, estado)
        self.transiciones.append(transicion)

    def derivar(self, caracter):
        return derivar(self.regex, caracter)
    
    def get_regex(self):
        return self.regex

    def set_nombre(self, x):
        self.nombre = f'q{x}'

    def get_nombre(self):
        return self.nombre

    def mostrar_transiciones(self):
        print(f'Estado {self.nombre}')
        for x in self.transiciones:
            print(f'{x.get_caracter()} -> {x.get_estado().get_nombre()}')

    def retornar_transiciones(self):
        texto = f'{self.nombre}:\n'
        for x in self.transiciones:
            texto = texto + f'{x.get_caracter()} -> {x.get_estado().get_nombre()}\n'
        return texto
