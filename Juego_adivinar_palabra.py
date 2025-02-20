import random
import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 500


# Imprimir reglas
def imprimir_reglas():
    print("""
      
🎉 Bienvenido a ahorcadito 🎉:

    Reglas:
    
      1. Una palabra será seleccionada de manera aleatoria y usted tendrá que adivinar la palabra.
      2. La palabra podrá ser adivinada de dos formas: adivinando letra por letra o adivinando la palabra completa.
      3. Cada letra que no adivine formará la figura del muñeco de palos ahorcado.
      4. Si la figura se completa, usted perderá.
      5. Si la palabra es adivinada, usted gana.
      
Entendido esto, ¡vamos a empezar!
      """)


# Lista de palabras aleatorias
def palabra_aleatoria():
    palabras = [
        "avion", "elefante", "computadora", "universo", "relampago", 
        "bicicleta", "murcielago", "astronauta", "guitarra", "ventilador", 
        "hipopotamo", "espejismo", "orquesta", "mariposa", "tornillo", 
        "helipuerto", "camaleon", "sandwich", "destornillador", "biblioteca"
    ]
    return list(random.choice(palabras))
palabra_secreta = palabra_aleatoria()
length = len(palabra_secreta) # Longitud de la palabra secreta

# Verificar si el valor de entrada es valido
def verificar():
    while True:
        letra = input("\nPor favor ingresa una letra: ").strip().lower()
        if letra.isdigit():
            print("\n✖️  No ingrese dígitos, inténtelo nuevamente: ")
        elif len(letra) > 1:
            print("\n✖️  Por favor ingrese únicamente una letra: ")
        else:
            return letra

# Bucle para cambiar la letra correcta
def letra_correct():
    for i, char in enumerate(palabra_secreta): # i == indice, char == valor de primera iteracion
        if letra == char:
            palabra_formada[i] = letra
    print(f"\n✅  ¡Letra {letra} correcta!")

# Mostrar el estado del juego
def mostrar_estado():
    if palabra_secreta == palabra_formada:
        print(f"\n🎉 Palabra Completada 🎉 {"".join(palabra_formada)}" )
    print(f"\nHasta el momento, la palabra formada está así: {"".join(palabra_formada)}")
    print(f'\nLetras incorrectas: {", ".join(letras_erroneas)}')

# 
def letra_incorrect():
    if letra not in letras_erroneas:
        letras_erroneas.append(letra)
        print(f'\n❌ Letra {letra} incorrecta!')
    else:
        print(f"\n⚠️  Ya intentaste con la letra '{letra}'")
    print(AHORCADO[len(letras_erroneas)-1])

def verificar_palabra():
    if len(letras_erroneas) == len(AHORCADO):
        print("\n🚫  ¡Perdiste! La palabra era: ", "".join(palabra_secreta))
        return True
    elif palabra_secreta == palabra_formada:
        print("\n🎉  ¡Ganaste! La palabra es:","".join(palabra_secreta))
        return True
    return False

#Iniciar el juego
imprimir_reglas()
print(f"La palabra contiene un total de {length} letras") # Num de letras de la palabra
palabra_formada = ["_" for _ in range(length)]
letras_erroneas = []
AHORCADO = [''' 
  +---+  
  |   |  
      |  
      |  
      |  
      |  
=========''','''  
  +---+  
  |   |  
  O   |  
      |  
      |  
      |  
=========''','''  
  +---+  
  |   |  
  O   |  
  |   |  
      |  
      |  
=========''','''  
  +---+  
  |   |  
  O   |  
 /|   |  
      |  
      |  
=========''','''  
  +---+  
  |   |  
  O   |  
 /|\  |  
      |  
      |  
=========''','''  
  +---+  
  |   |  
  O   |  
 /|\  |  
 /    |  
      |  
=========''','''  
  +---+  
  |   |  
  O   |  
 /|\  |  
 / \  |  
      |  
=========''']



while palabra_secreta != palabra_formada:
    print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    letra = verificar()
    if letra in palabra_secreta:
        letra_correct()
    else:
        letra_incorrect()
    mostrar_estado()
    if verificar_palabra():
        break