import random

print("""
      
Bienvenido a ahorcadito:

    Reglas:
    
      1.Una palabra de sera seleccionada de manera aleatoria y usted tendra que adivinar la palabra
      2.La palabra podra ser adivinada de dos formas, o adivinando letra por letra o adivinando la palabra completa
      3.Cada letra que no adivine formara la figura del muñeco de palos ahorcado
      4.Si la figura se completa usted perdera
      5.Si la palabra es adivinada usted gana.  
      
Entendido esto vamos a empezar
      """)

#Lista de palabras aleatorias
palabras = [
    "avion", "elefante", "computadora", "universo", "relampago", 
    "bicicleta", "murcielago", "astronauta", "guitarra", "ventilador", 
    "hipopotamo", "espejismo", "orquesta", "mariposa", "tornillo", 
    "helipuerto", "camaleon", "sandwich", "destornillador", "biblioteca"
]
palabra_secreta = list(random.choice(palabras))
length = len(palabra_secreta)
count = 0
palabra_formada = ["_" for _ in range(length)]
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


print("_"*length, f"La palabra contiene un total de {length} letras") #Num de letras

while palabra_secreta != palabra_formada:
    
    #Input de letra
    if "_" in palabra_formada:
        if palabra_formada.count("_") == len(palabra_formada):  # Si todas las letras de palabra formada son "_"
            letra = input("\nEmpecemos con una letra: ")
        else:
            letra = input("\nContinuemos con otra letra: ") #Si hay alguna letra en la palabra formada
            
    #Verificar si letra esta en palabra secreta
    lista =[] #Lista de indices reiniciada en cada letra
    if letra in palabra_secreta:
        lista = [i for i in range(length) if palabra_secreta[i] == letra] #Indices de cada letra de palabra secreta
        for i in lista:
            palabra_formada[i] = letra #Cambio la letra en la palabra formada
        print(f'''\nLetra {letra} correcta! Hasta el momento, la palabra formada está así: {"".join(palabra_formada)}''')
        if palabra_formada == palabra_secreta: #Si la palabra se completa
            print(f"\nPalabra Completa!, La palabra era {"".join(palabra_secreta)}")

    else:
        if count >= len(AHORCADO): #Si alcanzo el maximo de intentos
            print(f"\nMaximo de intentos alcanzado, la palabra correcta era {palabra_secreta}")
            break
        print(f'{AHORCADO[count]} Hasta el momento, la palabra formada está así: {"".join(palabra_formada)}')
        count += 1
        
        
    


 








