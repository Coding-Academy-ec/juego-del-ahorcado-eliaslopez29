import random

AHORCADO_DIBUJO = [
    """
       |
    """,
    """
       |
       O
    """,
    """
       |
      /O
    """,
    """
       |
      /O\\
    """,
    """
       |
      /O\\
       |
    """,
    """
       |
      /O\\
       |
      /
    """,
    """
       |
      /O\\
       |
      / \\
    """
]


def seleccionar_palabra():
    """
    Selecciona y devuelve una palabra aleatoria de la lista.
    """
    palabras = ['python', 'programacion', 'desarrollo', 'ahorcado']
    return random.choice(palabras)


def mostrar_progreso(palabra, letras_adivinadas):
    """
    Devuelve una representación del progreso del jugador,
    mostrando letras adivinadas y guiones bajos para las letras no adivinadas.
    """
    progreso = ' '.join(
        letra if letra in letras_adivinadas else '_' for letra in palabra)
    return progreso


def verificar_letra(letra, palabra):
    """
    Verifica si la letra está en la palabra.
    """
    return letra in palabra


def juego_ahorcado():
    """
    Función principal del juego del ahorcado.
    Maneja el flujo del juego, solicitando letras y controlando los intentos.
    """
    palabra = seleccionar_palabra()
    letras_adivinadas = []
    intentos_fallidos = 0
    max_intentos = 6

    while intentos_fallidos < max_intentos:
        print(AHORCADO_DIBUJO[intentos_fallidos])
        print(mostrar_progreso(palabra, letras_adivinadas))
        letra = input("Adivina una letra: ").lower()

        if verificar_letra(letra, palabra):
            letras_adivinadas.append(letra)
            print("¡Correcto! 🎉")
        else:
            intentos_fallidos += 1
            print("Incorrecto 😢")

        # Comprobamos si se han adivinado todas las letras de la palabra.
        if all(letra in letras_adivinadas for letra in palabra):
            print(f"¡Felicidades, adivinaste la palabra: {palabra}!")
            break
    else:
        print(AHORCADO_DIBUJO[max_intentos])
        print(f"Perdiste. La palabra era: {palabra}")


if __name__ == "__main__":
    juego_ahorcado()

