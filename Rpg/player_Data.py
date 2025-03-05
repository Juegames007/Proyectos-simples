import json
import random
import keyboard
import images
import os
import time

class Player:
    estados = ["Ninguno", "inspirado","bendecido"]
    def __init__(self,name = None,gender = None,image = None,rol = None):
        
        self.name = name
        self.level = 0
        self.gender = gender
        self.image = image
        self.rol = rol
        self.mana = 10
        self.fisic_damage = 5
        self.estado = "Sin estados"
        self.hp = 100
        self.strength = random.randint(1, 10)
        self.defense = random.randint(1, 10)
        self.luck = random.randint(1, 10)
        # Atributos especiales
        self.charisma = random.randint(1, 10)
        self.hunger = 50  # Empieza con hambre moderada
        self.intelligence = random.randint(1, 10)
        self.experience = 0  # Empieza sin experiencia
        self.indice_gender = 0
        self.indice_rol = 0
        self.indice_name = 0
        self.yes_or_no =  ["Yes", "No"]
        self.male_female = ["Hombre", "Mujer"]
        self.Roles = {"Mago": "Personaje que usa mana para atacar y defenderse, su tipo de ataque es magico y es debil contra los ataques tipo daño fisico",
                 "Espadero" : "Personaje que depende de su estamina para atacar, es muy malo para defenderse pero buenisimo al atacar y es debil contra los ataques de escudo",
                  "Escudero": "Peronaje que tiene ataques especiales de escudo y altas estadisticas en defensa, es debil contra los ataque magicos" }
        
        if name is None:
            self.cargar_progreso()
    
    def guardar_progreso(self):
        estadisticas_jugador = {
            "name": self.name,
            "level": self.level,
            "gender": self.gender,
            "image":self.image,
            "rol":self.rol,
            "estado":self.estado,
            "hp":self.hp,
            "strength":self.strength,
            "defense":self.defense,
            "luck":self.luck ,
            "charisma":self.charisma,  
            "hunger":self.hunger,
            "intelligence":self.intelligence, 
            "experience":self.experience  
        }
        with open("Estadisticas jugador","w") as archivo_json:
            json.dump(estadisticas_jugador,archivo_json,indent=4)
        print("✅ Progreso guardado.")

    def cargar_progreso(self):
        try:
            with open("Estadisticas jugador", "r") as archivo:
                estadisticas_jugador = json.load(archivo)
                vars(self).update(estadisticas_jugador)  # Carga todo de una vez
            print(f"✅ Progreso cargado, nombre {self.name}")
        except FileNotFoundError:
            print("⚠️ No existe progreso guardado")
    
    def confirm_input_nombre(self):
        os.system("cls")
        print("\n Estas seguro de que ese es tu nombre?")
        for i, y_n in enumerate(self.yes_or_no):
            if self.indice_name == i:
                print(f"\n 👉 {y_n} 👈 ")
            else:
                print(f"\n     {y_n}    ")

    def keyboard_(self ,indice ,output_msg ,length ,options, input, print_funtion):
        while True:
            event = keyboard.read_event()
            if event.event_type == "down":
                if event.name == "flecha abajo":
                    indice = (indice + 1) % length
                elif event.name == "flecha arriba":
                    indice = (indice - 1) % length
                elif event.name == "enter":
                    print(output_msg)
                    return options[indice]
                else:
                    continue
                print_funtion() 
    def input_nombre(self):
        self.name = str(input("\nCual es tu nombre?: \n"))
        while True: #Name
            self.name = str(input("\nCual es tu nombre?: \n"))
            event = keyboard.read_event()
            if event.event_type == "down":
                if event.name == "flecha abajo":
                    self.indice_name = (self.indice_name + 1) % self.length_name
                elif event.name == "flecha arriba":
                    self.indice_name = (self.indice_name)
                elif event.name == "enter":



            

    def print_male_o_female(self):    
        os.system("cls")
        print("\nEres hombre o mujer? \n")
        for i, genero in enumerate(self.male_female):
            if self.indice_gender == i:
                print(f"\n 👉 {genero} 👈")
            else:
                print(f"\n    {genero}    ")
                
    def input_gender(self):
        self.length_gender = len(self.male_female)
        while True:
            event = keyboard.read_event()
            if event.event_type == "down":
                if event.name == "flecha abajo":
                    self.indice_gender = (self.indice_gender + 1) % self.length_gender
                elif event.name == "flecha arriba":
                    self.indice_gender = (self.indice_gender - 1) % self.length_gender
                elif event.name == "enter":
                    print(f"Asi que eres un {self.male_female[self.indice_gender]}, pues bienvenido!! ")
                    self.gender = self.male_female[self.indice_gender]
                    break
                else:
                    continue
                self.print_male_o_female() 
                time.sleep(0.1)
            

    def input_image(self):
        if self.gender == self.male_female[0]:
            image = images.images_male[0]
            print(f"\nSorpresa de la vida, asi te ves : \n\n{image}\n")
            self.image = image
        else:
            image = images.image_female[1]
            print(f"\nSorpresa de la vida, asi te ves : \n\n{image}")
            self.image = image
    

    def print_rol(self):
        os.system("cls")
        print(f"Es la hora de escojer tu rol: {self.Roles}")
        for i, genero in enumerate(self.Roles):
            if self.indice_rol == i:
                print(f"\n 👉 {genero} 👈")
            else:
                print(f"\n    {genero}    ")

    def input_rol(self):
        self.length_roles = len(self.Roles)
        while True:
            event = keyboard.read_event()
            if event.event_type == "down":
                if event.name == "flecha abajo":
                    self.indice_rol = (self.indice_rol + 1) % self.length_roles
                    Player.print_rol(self)
                elif event.name == "flecha arriba":
                    self.indice_rol = (self.indice_rol - 1) % self.length_roles
                    Player.print_rol(self)
                elif event.name == "enter":
                    keys = list(self.Roles.keys())  # Obtiene solo los nombres de los roles
                    rol = keys[self.indice_rol]  # Guarda solo el nombre del rol
                    self.rol = rol
                    print(f"Te aventuras a ser {rol}, Ojalá te vaya bien en tu aventura")
                    break
                else: 
                    continue
                time.sleep(0.1)

jugador1 = Player()
# Llamar a las funciones de entrada
    # def aumento_stats(self):

        

    


    
        


            
    # def inventario(self):
        # self.slot_1 = None
        # self.slot_2 = None
        # self.slot_3 = None
        # self.slot_4 = None
        # self.slot_5 = None
    
    # def equipamiento(self):
        # self.armadura = None
        # self.arma = None