import random
import os

animales = [
    'perro', 'gato', 'elefante', 'tigre', 'leon', 'jirafa',
    'zebra', 'panda', 'koala', 'canguro', 'oso', 'lobo',
    'zorro', 'ciervo', 'rinoceronte', 'hipopotamo', 'buho',
    'aguila', 'flamenco', 'pinguino', 'tortuga',
    'delfin', 'ballena', 'tiburon', 'cocodrilo', 'serpiente',
    'rana', 'murcielago', 'ardilla'
]

frutas = [
    'manzana', 'melocoton', 'platano', 'sandia',
    'cereza', 'naranja', 'mandarina', 'fresa'
]

colores = [
    'rojo', 'azul', 'verde', 'amarillo', 'naranja', 'morado',
    'rosa', 'marron', 'negro', 'blanco', 'gris', 'turquesa',
    'lavanda', 'dorado', 'plateado', 'fucsia', 'cyan', 'magenta',
    'ocre', 'salmon', 'vino', 'lima', 'oliva',
    'esmeralda', 'caramelo', 'ambar', 'ciruela', 'lavanda'
]


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


def print_banner():
    """
    Imprime un banner con arte ASCII.

    Esta función no toma ningún parámetro.

    Esta función no devuelve nada.
    """

    print(r"""
      ___                                  ___           ___           ___           ___           ___           ___          _____          ___     
     /  /\                                /  /\         /__/\         /  /\         /  /\         /  /\         /  /\        /  /::\        /  /\    
    /  /:/_                              /  /::\        \  \:\       /  /::\       /  /::\       /  /:/        /  /::\      /  /:/\:\      /  /::\   
   /  /:/ /\    ___     ___             /  /:/\:\        \__\:\     /  /:/\:\     /  /:/\:\     /  /:/        /  /:/\:\    /  /:/  \:\    /  /:/\:\  
  /  /:/ /:/_  /__/\   /  /\           /  /:/~/::\   ___ /  /::\   /  /:/  \:\   /  /:/~/:/    /  /:/  ___   /  /:/~/::\  /__/:/ \__\:|  /  /:/  \:\ 
 /__/:/ /:/ /\ \  \:\ /  /:/          /__/:/ /:/\:\ /__/\  /:/\:\ /__/:/ \__\:\ /__/:/ /:/___ /__/:/  /  /\ /__/:/ /:/\:\ \  \:\ /  /:/ /__/:/ \__\:\
 \  \:\/:/ /:/  \  \:\  /:/           \  \:\/:/__\/ \  \:\/:/__\/ \  \:\ /  /:/ \  \:\/:::::/ \  \:\ /  /:/ \  \:\/:/__\/  \  \:\  /:/  \  \:\ /  /:/
  \  \::/ /:/    \  \:\/:/             \  \::/       \  \::/       \  \:\  /:/   \  \::/~~~~   \  \:\  /:/   \  \::/        \  \:\/:/    \  \:\  /:/ 
   \  \:\/:/      \  \::/               \  \:\        \  \:\        \  \:\/:/     \  \:\        \  \:\/:/     \  \:\         \  \::/      \  \:\/:/  
    \  \::/        \__\/                 \  \:\        \  \:\        \  \::/       \  \:\        \  \::/       \  \:\         \__\/        \  \::/   
     \__\/                                \__\/         \__\/         \__\/         \__\/         \__\/         \__\/                       \__\/                                                                                                                                      

    """)


def print_welcome():
    print("""
Bienvenido al juego del Ahorcado, dispones de 10 intentos para descubrir la palabra secreta. Preparate para el desafío!!
    """)


def modo_dificil(lista):
    """
    Selecciona una palabra aleatoria de la lista dada y genera una versión oculta de ella.

    Args:
        lista (lista): Una lista de palabras.

    Returns:
        tuple: Un tupla que contiene la palabra seleccionada aleatoriamente y su versión oculta.
            La versión oculta es una lista de guiones con la misma longitud que la palabra.
    """

    # Selecciona una palabra aleatoria de la lista dada
    palabra = random.choice(lista)
    # Crea una lista con las letras de la palabra
    lista_de_letras = list(palabra)
    # Genera una lista de letras ocultas con el 80% de las letras de la palabra
    palabra_oculta = random.sample(
        lista_de_letras, int(len(lista_de_letras) * 0.8))

    # Reemplaza las letras ocultas en la lista de letras por guiones bajos
    for letra in palabra_oculta:
        lista_de_letras[lista_de_letras.index(letra)] = '_'

    # Convierte la lista de letras en una cadena
    palabra_oculta = ''.join(lista_de_letras)

    # Retorna la palabra seleccionada y su versión oculta
    return palabra, palabra_oculta


def modo_facil(lista):
    """
    Generates a version of a randomly selected word from the given list with 80% of its letters replaced by underscores.

    Parámetros:
    - lista (list): Una lista de palabras.

    Retorna:
    - tupla: Una tupla que contiene la palabra seleccionada aleatoriamente y su versión con guiones bajos.
    """

    # Selecciona una palabra aleatoria de la lista dada
    palabra = random.choice(lista)
    # Crea una lista con las letras de la palabra
    lista_de_letras = list(palabra)
    # Genera una lista de letras ocultas con el 80% de las letras de la palabra
    palabra_oculta = random.sample(
        lista_de_letras, int(len(lista_de_letras) * 0.8))

    # Reemplaza las letras ocultas en la lista de letras por guiones bajos
    for letra in palabra_oculta:
        lista_de_letras[lista_de_letras.index(letra)] = '_'

    # Convierte la lista de letras en una cadena
    palabra_oculta = ''.join(lista_de_letras)

    # Retorna la palabra seleccionada y su versión oculta
    return palabra, list(palabra_oculta)


def main():
    """
    La función principal del programa. Permite al usuario elegir un grupo de palabras para adivinar una palabra oculta.
    El usuario puede elegir jugar en modo Experto o Principiante.
    El programa genera una palabra aleatoria del grupo elegido y la presenta al usuario como palabra oculta.
    El usuario tiene 10 intentos para adivinar la palabra.
    Si el usuario adivina correctamente una letra, se revela en la palabra oculta.
    Si el usuario adivina incorrectamente una letra, pierde un intento.
    Si el usuario adivina correctamente toda la palabra, gana.
    Si el usuario se queda sin intentos, pierde.

    Parámetros:
    Ninguno

    Retorna:
    Ninguno
    """

    clear_screen()
    print_banner()
    print_welcome()

    print('Puedes elegir descubrir la palabra secreta entre tres grupos diferentes de palabras.')

    print("""
    \nElige un grupo:

      [1] Animales
      [2] Frutas
      [3] Colores
      """)

    grupo = input('Selecciona una opción: ')

    if grupo == '1':
        print('\nPerfecto, has decidido descubrir cuál es el animal oculto en la palabra secreta.')
        print('Tambien puedes elegir juegar en modo EXPERTO o PRINCIPIANTE.')

        opcion = input(
            'Quieres jugar al modo EXPERTO (Si/No)? > ').lower().strip()

        if opcion == 'si':
            palabra_al_azar, palabra_oculta = modo_dificil(animales)
        else:
            palabra_al_azar, palabra_oculta = modo_facil(animales)

    elif grupo == '2':
        print('\nPerfecto, has decidido descubrir cuál es la fruta oculta en la palabra secreta.')
        print('Tambien puedes elegir juegar en modo EXPERTO o PRINCIPIANTE.')

        opcion = input(
            'Quieres jugar al modo EXPERTO (Si/No)? > ').lower().strip()

        if opcion == 'si':
            palabra_al_azar, palabra_oculta = modo_dificil(frutas)
        else:
            palabra_al_azar, palabra_oculta = modo_facil(frutas)

    elif grupo == '3':
        print('\nPerfecto, has decidido descubrir cuál es el color oculto en la palabra secreta.')
        print('Tambien puedes elegir juegar en modo EXPERTO o PRINCIPIANTE.')

        opcion = input(
            'Quieres jugar al modo EXPERTO (Si/No)? > ').lower().strip()

        if opcion == 'si':
            palabra_al_azar, palabra_oculta = modo_dificil(colores)
        else:
            palabra_al_azar, palabra_oculta = modo_facil(colores)

    else:
        print("Opción no válida. Elige un número entre 1 y 3.")
        return

    print('\nEsta es la palabra secreta, recuerda que tienes 10 intentos. Suerte!!')

    intentos = 10

    while palabra_oculta != list(palabra_al_azar) and intentos > 0:
        print(f'\n{" ".join(palabra_oculta)}')

        letra = input('\nIntroduce una letra: ').lower().strip()

        if letra in palabra_al_azar:
            for idx, caracter in enumerate(palabra_al_azar):
                if letra == caracter:
                    palabra_oculta[idx] = letra

            print('\nHas descubierto una letra dentro de la palabra oculta. ¡Bien hecho!')

            if palabra_oculta == list(palabra_al_azar):
                print(f'\n{" ".join(palabra_oculta)}')
                print('\n¡Lo has conseguido! Has descifrado la palabra secreta.')
                print(f"\nLa palabra oculta era \"{
                      ''.join(palabra_al_azar)}\"")
                break
        else:
            print('\n¡Oh no! La letra introducida no se encuentra en la palabra oculta.')
            intentos -= 1
            print(f'\nTe quedan {
                  intentos} intentos para descubrir la palabra secreta.')
            print(f'\nLetras encontradas: {", ".join(
                [letra for letra in palabra_oculta if letra != "_"])}')

    if palabra_oculta != list(palabra_al_azar):
        print(f'\nLo siento, has perdido. La palabra secreta era "{
              palabra_al_azar}".')


if __name__ == "__main__":
    main()
