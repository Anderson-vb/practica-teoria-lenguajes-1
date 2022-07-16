from distutils.log import info
from re import I
from estado import Estado

class AFD:

    def __init__(self):
        self.estados = []

    def crear_afd(self, estado_inicial):
        lista_simbolos = []
        lista_estados = []
        lista_estados.append(estado_inicial)
 
        # Obtenemos todos los caracteres (a, b, c, 0, 1, etc) que tiene la expresion regular
        # y los guardamos en el array lista_simbolos 
        for x in estado_inicial.get_regex():
            if x != '+' and x != '*' and x != '(' and x != ')':
                lista_simbolos.append(x)
 
        for estado in lista_estados:
            for simbolo in lista_simbolos:
                # Derivamos el estado y obtenemos el nuevo estado
                nuevo_estado = Estado(estado.derivar(simbolo))
 
                if nuevo_estado.get_regex() == estado.get_regex():
                    estado.add_transicion(simbolo, estado)
                else:
                    estados_iguales = False
                    for x in lista_estados:
                        if nuevo_estado.get_regex() == x.get_regex() or f'({nuevo_estado.get_regex()})' == x.get_regex() or nuevo_estado.get_regex() == f'({x.get_regex()})':
                            estado.add_transicion(simbolo, x)                    
                            estados_iguales = True
                    if not estados_iguales:
                        estado.add_transicion(simbolo, nuevo_estado)
                        lista_estados.append(nuevo_estado)
                    
        for x in lista_estados:
            if x.get_regex() == '()':
                lista_estados.remove(x)

        for x in range(len(lista_estados)):
            lista_estados[x].set_nombre(x + 1)


        self.estados = lista_estados
    

    def get_estados(self):
        return self.estados

    def mostrar_afd(self):
        informacion = ''
        for x in self.get_estados():
            informacion = informacion + f'{x.get_nombre()}: {x.get_regex()}\n'

        informacion = informacion + '\n'

        for x in self.get_estados():
            informacion = informacion + f'{x.retornar_transiciones()}\n'
 
        return informacion

