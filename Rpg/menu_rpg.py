import os
import keyboard
from player_Data import Player

class menu:
    def __init__(self):
        self.opciones = ["Jugar 🎮", "Cargar Progreso 💾","Exit 🔚"]
        self.indice = 0
        self.length_menu = len(self.opciones)
    def mostrar_menu(self):
        os.system("cls")  # Limpia la pantalla en Windows
        print("\n" + "=" * 40)
        print(" " * 9 + "🎮  🕹️   M E N Ú   🕹️   🎮")
        print("=" * 40 + "\n")

        for i, opcion in enumerate(self.opciones):
            if self.indice == i:
                print(f"           👉   {opcion}  👈")  # Flechas para indicar selección
            else:
                print(f"                {opcion}")

        print("\n" + "=" * 40)
    
    def seleccion_opcion(self):
        while True:
            event = keyboard.read_event()
            if event.event_type == "down":
                if event.name == "flecha abajo":
                    self.indice = (self.indice + 1) % self.length_menu
                    menu.mostrar_menu(self) 
                if event.name == "flecha arriba":
                    self.indice = (self.indice - 1) % self.length_menu
                    menu.mostrar_menu(self) 
                if event.name == "enter":
                    if self.indice == 0:
                        print("Iniciando una nueva partida... ")
                        self.iniciar_partida()
                    if self.indice == 1:
                        print("Cargando la partida guardada... ")
                    if self.indice == 2:
                        print("Saliendo del juego... ")
                        exit()
            else:
                continue
    
    @staticmethod
    def mostrar_tutorial():
        print("\n" + "=" * 50)
        print("🕹️  BIENVENIDO A TU PESADILLA 🕹️".center(50))
        print("=" * 50 + "\n")
    
        print("Te despiertas en un edificio abandonado con 8 pisos.")
        print("Una voz en tu cabeza susurra que la única forma de salir es llegar a la cima.")
        print("Pero no será fácil... Cada piso tiene sus propios peligros y desafíos.\n")

        print("📜 **REGLAS DEL JUEGO** 📜\n")
        print("🔹 El avance es **lineal**, no puedes volver atrás.")
        print("🔹 Para escapar, debes subir **8 pisos**.")
        print("🔹 Cada piso tiene enemigos y eventos aleatorios.")
        print("🔹 Debes administrar tu **vida, hambre y energía** sabiamente.")
        print("🔹 A veces, correr es mejor que pelear... pero no siempre.")
        print("🔹 **No estarás solo**: tendrás a un compañero en tu equipo.")
        print("   📌 Cada uno tiene habilidades únicas y puede marcar la diferencia en combate o exploración.\n")
        
        print("⚠️ *¿Sobrevivirás lo suficiente para alcanzar la libertad?* ⚠️")

    def iniciar_partida(self):
        self.mostrar_tutorial()
        jugador1 = Player()
        jugador1.input_nombre()

    
        




        
        

                
    
                
Menu = menu()
Menu.mostrar_menu()
Menu.seleccion_opcion()