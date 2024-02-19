'''
Encapsulando el juego en una clase

Ahora que disponemos de muchas más herramientas, podemos notar que reutilizamos la variable que contiene el mapa muchas veces y es molesto llamar funciones desconectadas enviando el mismo parámetro.

La programación orientada a objetos viene a nuestro rescate!

Implementa la clase Juego, ahora el mapa y las posiciones inicial y final son atributos de esta clase, reescribe todas tus funciones anteriores de forma que sean métodos de la clase y todo esté encapsulado.

Instanciar el juego y ejecutarlo desde el main
Almacenando mapas en archivos

En lugar de almacenar el mapa en el mismo código, podemos guardarlo en archivos con sus posiciones de inicio y fin y las dimensiones del mapa en la primera línea del archivo, de esta manera los componentes de la aplicación estarán separados y podremos mejorar la experiencia del juego.

    Crear una nueva clase JuegoArchivo la cual hereda de Juego,
    Reescribir el constructor para leer un archivo al azar de una carpeta que contenga los mapas cada vez que se instancia el juego.
        Para listar los archivos de un directorio usar os.listdir(path) , esto devolverá una lista con el nombre los archivos en ese directorio
        Para elegir un elemento aleatorio de una lista usar random.choice(lista).
        Note que para poder leer el archivo tenemos que componer el path, una forma de hacerlo es path_completo = f"{path_a_mapas}/{nombre_archivo}"
    Crear un método que lea los datos de estos archivos de mapa y devuelva una cadena que tenga concatenada todas las filas leídas del mapa y las coordenadas de inicio y fin. Al final de la lectura antes de retornar usar cadena.strip() para eliminar caracteres en blanco residuales.

'''

import os
import random  # Agrega esta línea
from readchar import readkey, key

class Juego:
    def __init__(self, mapa, posicion_inicial, posicion_final):
        self.mapa = mapa
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final
        self.px, self.py = posicion_inicial

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_mapa(self):
        self.limpiar_pantalla()
        for fila in self.mapa:
            print("".join(fila))

    def verificar_posicion_valida(self, px, py):
        return 0 <= px < len(self.mapa[0]) and 0 <= py < len(self.mapa) and self.mapa[py][px] != "#"

    def actualizar_posicion(self, tecla):
        nueva_px, nueva_py = self.px, self.py

        if tecla == key.UP and self.py > 0 and self.mapa[self.py - 1][self.px] != '#':
            nueva_py -= 1  # Flecha arriba
        elif tecla == key.DOWN and self.py < len(self.mapa) - 1 and self.mapa[self.py + 1][self.px] != '#':
            nueva_py += 1  # Flecha abajo
        elif tecla == key.LEFT and self.px > 0 and self.mapa[self.py][self.px - 1] != '#':
            nueva_px -= 1  # Flecha izquierda
        elif tecla == key.RIGHT and self.px < len(self.mapa[0]) - 1 and self.mapa[self.py][self.px + 1] != '#':
            nueva_px += 1  # Flecha derecha

        if self.verificar_posicion_valida(nueva_px, nueva_py):
            return nueva_px, nueva_py
        else:
            return self.px, self.py

    def main_loop(self):
        while (self.px, self.py) != self.posicion_final:
            self.mapa[self.py][self.px] = "P"
            self.mostrar_mapa()

            # Leer la tecla presionada
            tecla = readkey()

            # Restaurar la posición anterior antes de verificar si la nueva posición es válida
            self.mapa[self.py][self.px] = "."

            # Actualizar la posición tentativa
            self.px, self.py = self.actualizar_posicion(tecla)
        
        self.mostrar_mapa()
        print("¡Has logrado salir del Laberinto, nos vemos en el siguiente módulo!")
        input("Presiona Enter para salir...")  # Agregue esta línea
        self.mapa[self.py][self.px] = "P"  # Mostrar la posición final

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        mapa, pos_inicial, pos_final = self.leer_mapa_aleatorio(path_a_mapas)
        super().__init__(mapa, pos_inicial, pos_final)

    def leer_mapa_aleatorio(self, path_a_mapas):
        archivos_mapas = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(archivos_mapas)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        with open(path_completo, 'r') as archivo:
            contenido = archivo.read()

        return self.extraer_datos_mapa(contenido)

    def extraer_datos_mapa(self, contenido):
        lineas = contenido.strip().split("\n")
        mapa = [list(linea) for linea in lineas[1:]]
        posiciones = lineas[0].split()
        pos_inicial = tuple(map(int, posiciones[:2]))
        pos_final = tuple(map(int, posiciones[2:]))
        return mapa, pos_inicial, pos_final

# Ejemplo de uso
path_a_mapas = os.path.join(os.path.dirname(__file__), "Mapas")
juego = JuegoArchivo(path_a_mapas)
juego.main_loop()
