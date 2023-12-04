from readchar import readkey, key

print("¡Bienvenido al Juego del Laberinto!")
print("Presiona una tecla para moverte. Para salir, presiona la tecla 'UP'.")

while True:
    # Lee un carácter del teclado
    tecla = readkey()

    # Verifica si la tecla es la flecha hacia arriba (UP)
    if tecla == key.UP:
        break

    # Imprime la tecla presionada y una acción ficticia
    print(f"Tecla presionada: {tecla}")
    print("Realizando una acción ficticia...")

print("¡Gracias por jugar! Programa finalizado.")