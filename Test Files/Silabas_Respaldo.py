import os

class separador_silaba:
    consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"] #!
    grupo_consonante_no_separar = ["pl", "pr", "bl", "br", "cl", "cr", "fl", "fr", "gl", "gr", "dr", "tr", "ch", "ll", "rr","tl"] #2
    vocales = ["a","e","i","o","u","á","é","í","ó","ú"] #3
    vocales_abiertas = ["a","e","o","á","é","ó"] #4
    vocales_cerradas = ["i","u"] #5
    vocales_cerradas_tilde = ["í","ú"] #6
    diptongo = ["ai","ái","au","áu",
                "ei","éi","eu","éu",
                "ia","iá","ié","ie","io","ió","iu","iú",
                "oi","ói","ou","óu",
                "ua","uá","ue","ué","uo","uó","úi","ui"] #7
    hiato = [
    "aa", "aá", "áa", "ae", "aé", "áe", "aí", "ao", "aó", "áo", "aú",
    "ea", "éa", "eá", "ee", "ée", "eé", "eí", "eo", "éo", "eó", "eú",
    "ía", "íe", "ío",
    "oa", "óa", "oá", "oe", "óe", "oé", "oí", "oo", "óo", "oó", "oú",
    "úa", "úe", "úo"]#8
    
    def __init__(self,word = "Hola"):
        self.word = word.lower()
        self.tipo_de_letra = []
    
    def main(self):

        def agregar_dos_letras(indicee,num_type):
            self.tipo_de_letra.append((self.word[indicee] + self.word[indicee + 1],num_type))
        def omitir_letra_final(indicee,grupo):
            if indicee > 0 and self.word[indicee-1] + self.word[indicee] in grupo:
                return True
            
        for indice,letra in enumerate(self.word):

            #Consonantes
            if letra in self.consonantes:
                if self.es_grupo_inseparable(indice): #Inseparables 2
                    agregar_dos_letras(indice,2)
                elif omitir_letra_final(indice,self.grupo_consonante_no_separar):
                    continue

                else:
                     self.tipo_de_letra.append((letra, 1)) #Consonantes 1

            #Vocales
            if letra in self.vocales:

                #Diptongo
                if self._es_diptongo(indice): #Diptongo 7
                    agregar_dos_letras(indice,7)
                elif omitir_letra_final(indice,self.diptongo): 
                    continue

                #Hiato
                elif self._es_hiato(indice): #Hiato 8
                    self.tipo_de_letra.append((self.word[indice],8))
                # elif omitir_letra_final(indice,self.hiato):
                #     self.tipo_de_letra.append((self.word[indice],8))

                else:
                    self.clasificar_vocales(indice) #Vocales


    def clasificar_vocales(self,indice):
        """
        Clasifica las vocales de la palabra considerando:
        - Diptongos
        - Vocales con tilde
        - Vocales abiertas y cerradas
        """
        if self.word[indice] in self.vocales_abiertas:
            self.tipo_de_letra.append((self.word[indice], 4)) #Abiertas 4
            return True
        elif self.word[indice] in self.vocales_cerradas:
            self.tipo_de_letra.append((self.word[indice], 5)) #Cerradas 5
            return True
        elif self.word[indice] in self.vocales_cerradas_tilde:
            self.tipo_de_letra.append((self.word[indice], 6)) #Cerradas tilde 6
            return True
        return False

    def _es_hiato(self,indice):
        if indice != len(self.word) - 1:
            if self.word[indice] + self.word[indice + 1] in self.hiato:
                return True
        return False

    def _es_diptongo(self, indice):
       
        # No es el último carácter
        if indice < len(self.word) - 1: # si el Indice es menor a el ultimo indice
            # Comprobar diptongo hacia adelante
            if self.word[indice] + self.word[indice + 1] in self.diptongo:
                return True
            
    def es_grupo_inseparable(self,indice):
            if indice < len(self.word) - 1:
                if self.word[indice] + self.word[indice + 1] in self.grupo_consonante_no_separar: #Si indice < [-1]
                    return True                    # Si letra + letra es grupo inseparable
            return False

    def separar_silabas(self):
        self.silabas = []
        primeros_elementos = [x[0] for x in self.tipo_de_letra] #Letras (c,a,b,a,ll,o)
        segundos_elementos = [x[1] for x in self.tipo_de_letra] #Numeros (1,4,1,4,2,4)
        #V = Vocal
        #C = Consonante
        #D = Diptongo
        #H = Hiato
        #I = Inseparable

        una_letra_dos_caracteres = {
            84: "H + V",
            85: "H + V", 
            86: "H + V", 
            88: "H + V"
        }

        una_letra_tres_caracteres = { # Una letra equivale al indice de la letra que se separa Ej: a-vi a-mo
            414: "#V + C + V",
            415: "#V + C + V", 
            416: "#V + C + V",
            514: "#V + C + V", 
            515: "#V + C + V", 
            516: "#V + C + V",
            614: "#V + C + V", 
            615: "#V + C + V", 
            616: "#V + C + V",
            
            417: "#V + C + D", 
            517: "#V + C + D", 
            617: "#V + C + D",
            
            424: "#V + I + V", 
            425: "#V + I + V", 
            426: "#V + I + V",
            524: "#V + I + V", 
            525: "#V + I + V", 
            526: "#V + I + V",
            624: "#V + I + V", 
            625: "#V + I + V", 
            626: "#V + I + V",
            
            418: "#V + C + H", 
            518: "#V + C + H", 
            618: "#V + C + H",
            
            714: "#D + C + V", 
            715: "#D + C + V", 
            716: "#D + C + V",
            
            172: "#C + D + I"
        }

        una_letra_cinco_caracteres = {
            41141: "V + C + C + V + C",
            41151: "V + C + C + V + C",
            41161: "V + C + C + V + C",
            51141: "V + C + C + V + C",
            51151: "V + C + C + V + C",
            51161: "V + C + C + V + C",
            61141: "V + C + C + V + C",
            61151: "V + C + C + V + C",
            61161: "V + C + C + V + C",
        }

        dos_letra_tres_caracteres = { # Dos letra equivale al indice de la letra que se separa Ej: Bra(Br cuenta como un caracter)-
            284: "#I + H + V",
            285: "#I + H + V", 
            286: "#I + H + V",
            
            184: "#C + H + V", 
            185: "#C + H + V", 
            186: "#C + H + V",
            
            242: "#I + V + I", 
            252: "#I + V + I", 
            262: "#I + V + I",
            
            142: "#C + V + I", 
            152: "#C + V + I", 
            162: "#C + V + I",
            
            412: "#V + C + I", 
            512: "#V + C + I", 
            612: "#V + C + I",

            171: "C + D + C"
        }

        dos_letras_cuatro_caracteres = {
            4114: "#V + C + C + V", 
            4115: "#V + C + C + V", 
            4115: "#V + C + C + V",
            5114: "#V + C + C + V", 
            5115: "#V + C + C + V", 
            5116: "#V + C + C + V",
            6114: "#V + C + C + V", 
            6115: "#V + C + C + V", 
            6116: "#V + C + C + V",
            
            4117: "#V + C + C + D", 
            5117: "#V + C + C + D", 
            6117: "#V + C + C + D",
            
            1414: "#V + C + I + D", 
            1415: "#V + C + I + D", 
            1416: "#V + C + I + D",
            1514: "#V + C + I + D", 
            1515: "#V + C + I + D", 
            1516: "#V + C + I + D",
            1614: "#V + C + I + D", 
            1615: "#V + C + I + D", 
            1616: "#V + C + I + D",
            
            1417: "#C + V + C + V", 
            1517: "#C + V + C + V", 
            1617: "#C + V + C + V",
            
            2714: "#C + V + C + D", 
            2715: "#C + V + C + D", 
            2716: "#C + V + C + D",
            
            1714: "#I + D + C + V", 
            1715: "#I + D + C + V", 
            1716: "#I + D + C + V",
            
            2414: "#I + V + C + V", 
            2415: "#I + V + C + V", 
            2416: "#I + V + C + V",
            2514: "#I + V + C + V", 
            2515: "#I + V + C + V", 
            2516: "#I + V + C + V",
            2614: "#I + V + C + V", 
            2615: "#I + V + C + V", 
            2616: "#I + V + C + V",
            
            2417: "#I + V + C + D", 
            2517: "#I + V + C + D", 
            2617: "#I + V + C + D",
            
            2418: "#I + V + C + H", 
            2518: "#I + V + C + H", 
            2518: "#I + V + C + H",
            
            1418: "#C + V + C + H", 
            1518: "#C + V + C + H", 
            1618: "#C + V + C + H",
            
            1724: "#C + D + I + V", 
            1725: "#C + D + I + V", 
            1726: "#C + D + I + V"
        }

        tres_letras_tres_caracteres = {
            241: "#I + V + C",
            251: "#I + V + C", 
            261: "#I + V + C"
        }

        tres_letras_cuatro_caracteres = {
            4112: "#V + C + C + I", 
            5112: "#V + C + C + I", 
            6112: "#V + C + C + I",
            
            1711: "#C + D + C + C",
            
            1412: "#C + V + C + I", 
            1512: "#C + V + C + I", 
            1612: "#C + V + C + I",
            
            2711: "#I + D + C + C"
        }

        tres_letras_cinco_caracteres = {
            14114: "#C + V + C + C + V", 
            14115: "#C + V + C + C + V", 
            14116: "#C + V + C + C + V",
            15114: "#C + V + C + C + V", 
            15115: "#C + V + C + C + V", 
            15116: "#C + V + C + C + V",
            16114: "#C + V + C + C + V", 
            16115: "#C + V + C + C + V", 
            16616: "#C + V + C + C + V",
            
            14117: "#C + V + C + C + D", 
            15117: "#C + V + C + C + D", 
            16117: "#C + V + C + C + D",
            
            24114: "#C + V + C + C + V", 
            24115: "#C + V + C + C + V", 
            24116: "#C + V + C + C + V",
            25114: "#C + V + C + C + V", 
            25115: "#C + V + C + C + V", 
            25116: "#C + V + C + C + V",
            26114: "#C + V + C + C + V", 
            26115: "#C + V + C + C + V", 
            26116: "#C + V + C + C + V",
            
            24117: "#C + V + C + C + D", 
            25117: "#C + V + C + C + D", 
            26117: "#C + V + C + C + D",
            
            24118: "#C + V + C + C + H", 
            25118: "#C + V + C + C + H", 
            26118: "#C + V + C + C + H"
        }

        cuatro_letras_cinco_caracteres = {
            14112: "#C + V + C + C + I", 
            15112: "#C + V + C + C + I", 
            16112: "#C + V + C + C + I",
            
            14112: "#C + V + C + C + I", 
            15112: "#C + V + C + C + I", 
            15112: "#C + V + C + C + I",
            
            24111: "#C + V + C + C + I", 
            25111: "#C + V + C + C + I", 
            26111: "#C + V + C + C + I",
            
            24112: "#C + V + C + C + I", 
            25112: "#C + V + C + C + I", 
            26112: "#C + V + C + C + I",
            
            14111: "#C + V + C + C + I", 
            15111: "#C + V + C + C + I", 
            16111: "#C + V + C + C + I",
            
            17711: "#C + V + C + C + I"
            }

        count = 0

        def separador_silabas(num_caracteres, diccionario,num_letras_agregar):
            if len(segundos_elementos) >= num_caracteres: #Si hay x elementos en la lista
                 codigo_formado = int("".join([str(segundos_elementos[i]) for i in range(num_caracteres)]))
                 if codigo_formado in diccionario:
                    self.silabas.append("".join([primeros_elementos[i] for i in range(num_letras_agregar)]))
                    del segundos_elementos[0:num_letras_agregar]
                    del primeros_elementos[0:num_letras_agregar]

                
        while True:
    
            #1 letra 5 caracteres
            hola = separador_silabas(5,una_letra_cinco_caracteres,1)

            ##3 letras 5 Caracteres
            separador_silabas(5,tres_letras_cinco_caracteres,3)    
            
            ##4 Letras 5 Caracteres
            separador_silabas(5,cuatro_letras_cinco_caracteres,4)

            ##2 letras 4 Caracteres
            separador_silabas(4,dos_letras_cuatro_caracteres,2)
    
            ##3 letras 4 Carecteres
            separador_silabas(4,tres_letras_cuatro_caracteres,3)     

            ##1 Letra 3 Caracteres
            separador_silabas(3,una_letra_tres_caracteres,1)
            
            #2 letras 3 Caracteres
            separador_silabas(3,dos_letra_tres_caracteres,2)
            
            ##3 letras 3 Caracteres
            separador_silabas(3,tres_letras_tres_caracteres,3)

            ##1 letras 2 caracteres
            separador_silabas(2,una_letra_dos_caracteres,1)

            count += 1
            if count > len(self.word):
                self.silabas.append("".join(primeros_elementos))
                break

while True:
    prueba = separador_silaba(input("Ingresa la palabra en español: "))
    prueba.main()
    print(prueba.tipo_de_letra)
    prueba.separar_silabas()
    print("Palabra en silabas:","-".join(prueba.silabas))
    if input("'Y' Para salir, cualquier otra tecla para continuar: ") == "Y":
        break
    os.system("cls")