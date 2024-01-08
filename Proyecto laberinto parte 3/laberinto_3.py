#Proyecto Integrador - Parte 3

"""El objetivo es comenzar con un número inicializado en 0, y en un bucle esperar la entrada de la tecla 'n' del teclado. 

Por cada vez que se presiona 'n', se borrará la terminal y se imprimirá el nuevo número, incrementándolo hasta llegar a 50.

Para llevar a cabo la operación de limpiar la terminal antes de mostrar el nuevo contenido, se ha creado una función específica. 

Se utiliza la instrucción os.system('cls' en sistemas Windows o 'clear' en otros sistemas) para lograr esto. Es necesario importar la biblioteca os."""

import os
from readchar import readkey

def borrar_y_imprimir(numero):
    # Borra la terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    # Imprime el nuevo número
    print(numero)

def main():
    numero = 0

    while numero < 50:
        # Espera la entrada de teclado 'n'
        print("Presiona 'n' para aumentar el número: ")
        tecla = readkey()

        if tecla == 'n':
            numero +=1
            borrar_y_imprimir(numero)
            
            if numero == 50:
                print("¡Has incrementado el número a 50!")
                break
        
        else:
            print("Tecla no válida. Por favor, presiona 'n'.")

if __name__ == "__main__":
    main()