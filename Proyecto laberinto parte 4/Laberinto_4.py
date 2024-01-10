'''
Proyecto integrador parte 4

    Implementar una función que reciba el mapa de un laberinto en forma de cadena, y lo convierta a matriz de caracteres.
        Utiliza el siguiente mapa:

        laberinto = """..###################
        ....#...............#
        #.#.#####.#########.#
        #.#...........#.#.#.#
        #.#####.#.###.#.#.#.#
        #...#.#.#.#.....#...#
        #.#.#.#######.#.#####
        #.#...#.....#.#...#.#
        #####.#####.#.#.###.#
        #.#.#.#.......#...#.#
        #.#.#.#######.#####.#
        #...#...#...#.#.#...#
        ###.#.#####.#.#.###.#
        #.#...#.......#.....#
        #.#.#.###.#.#.###.#.#
        #...#.#...#.#.....#.#
        ###.#######.###.###.#
        #.#.#.#.#.#...#.#...#
        #.#.#.#.#.#.#.#.#.#.#
        #.....#.....#.#.#.#.#
        ###################.."""

Los puntos inicial y final deben ser dados al crear el juego, usar las coordenadas (0,0) para el inicio y (len(mapa)-1, len(mapa[0])-1) para el final.
Recuerdo: Para separar por filas usar split("\n") y para convertir una cadena a una lista de caracteres usar list(cadena).

Escribir una función que limpie la pantalla y muestre la matriz (recibe el mapa en forma de matriz)
Implementar el main loop en una función (recibe el mapa en forma de matriz)

recibir: mapa List[List[str]], posicion inicial Tuple[int, int], posicion final Tuple[int, int].
definir dos variavles px y py que contienen las coordenadas del jugador, iniciar como los valores de la posición incial
procesar mientras (px, py) no coincida con la coordenada final.
asignar el caracter P en el mapa a las coordenadas (px, py) en todo momento.
leer del teclado las teclas de flechas, antes de actualizar la posición, verificar si esta posición tentativa:
No se sale del mapa
No es una pared
Si la nueva posición es válida, actualizar (px, py), poner el caracter P en esta nueva coordenada y restaurar la anterior a .
mostrar


'''

import os
from readchar import readkey, key

def convertir_mapa_a_matriz(laberinto):
    # Dividir el laberinto en filas
    filas = laberinto.split("\n")
    matriz = [list(fila) for fila in filas]
    return matriz

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_mapa(mapa):
    limpiar_pantalla()
    for fila in mapa:
        print("".join(fila))

def verificar_posicion_valida(px, py, mapa):
    return 0 <= px < len(mapa[0]) and 0 <= py < len(mapa) and mapa[py][px] != "#"

def actualizar_posicion(tecla, px, py, mapa):
    nueva_px, nueva_py = px, py

    if tecla == key.UP and py > 0 and mapa[py - 1][px] != '#':
        nueva_py -= 1  # Flecha arriba
    elif tecla == key.DOWN and py < len(mapa) - 1 and mapa[py + 1][px] != '#':
        nueva_py += 1  # Flecha abajo
    elif tecla == key.LEFT and px > 0 and mapa[py][px - 1] != '#':
        nueva_px -= 1  # Flecha izquierda
    elif tecla == key.RIGHT and px < len(mapa[0]) - 1 and mapa[py][px + 1] != '#':
        nueva_px += 1  # Flecha derecha

    if verificar_posicion_valida(nueva_px, nueva_py, mapa):
        return nueva_px, nueva_py
    else:
        return px, py

def main_loop(mapa, posicion_inicial, posicion_final):
    px, py = posicion_inicial

    while (px, py) != posicion_final:
        mapa[py][px] = "P"
        mostrar_mapa(mapa)

        # Leer la tecla presionada
        tecla = readkey()

        # Restaurar la posición anterior antes de verificar si la nueva posición es válida
        mapa[py][px] = "."

        # Actualizar la posición tentativa
        px, py = actualizar_posicion(tecla, px, py, mapa)

    print("¡Has logrado salir del Laberinto, nos vemos en el siguiente módulo!")

laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

mapa = convertir_mapa_a_matriz(laberinto)
posicion_inicial = (0, 0)
posicion_final = (len(mapa[0]) - 1, len(mapa) - 1)

main_loop(mapa, posicion_inicial, posicion_final)

