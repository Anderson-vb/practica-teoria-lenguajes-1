from estado import Estado
from operaciones import derivar
from afd import AFD

# hola mundo
# Obtenemos la expresion regular, la cual sera el estado inicial
regex = input('Ingresa la expresion regular: ')
estado_inicial = Estado(regex)

afd = AFD()

afd.crear_afd(estado_inicial)

for x in afd.get_estados():
    print(f'{x.get_nombre()}: {x.get_regex()}')

for x in afd.get_estados():
    print(f'{x.mostrar_transiciones()}')

