import os

class separador_silaba:
    consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"] #!
    grupo_consonante_no_separar = ["pl", "pr", "bl", "br", "cl", "cr", "fl", "fr", "gl", "gr", "dr", "tr", "ch", "ll", "rr"] #2
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
        primeros_elementos = [x[0] for x in self.tipo_de_letra] #Letras
        segundos_elementos = [x[1] for x in self.tipo_de_letra] #Numeros
        #V = Vocal
        #C = Consonante
        #D = Diptongo
        #H = Hiato
        #I = Inseparable

        una_letra_dos_caracteres = {84,85,86,88}
                                                #V + C + V                      #V + C + D                  #V + I + V                #V + C + H     #D + C + V     #C + D + I
        una_letra_tres_caracteres = {414,415,416,514,515,516,614,615,616,      417,517,617,     424,425,426,524,525,526,624,625,626,  418,518,618,  714,715,716,       172   }      


                                    #I + H + V              #C + H + V      #I + V + I      #C + V + I      #V + C + I
        dos_letra_tres_caracteres = {284,285,286,           184,185,186,    242,252,262,     142,152,162,  412,512,612}

                                                     #V + C + C + V                        #V + C + C + D                    
        dos_letras_cuatro_caracteres = {4114,4115,4115,5114,5115,5116,6114,6115,6116,     4117,5117,6117,     
                      
        #V + C + I + D                  #C + V + C + V                         #C + V + C + D       #I + D + C + V         
        1414,1415,1416,1514,1515,1516,1614,1615,1616,      1417,1517,1617,       2714,2715,2716,    1714,1715,1716,                                                            

                      #I + V + C + V                     #I + V + C + D     #I + V + C + H    #C + V + C + H   #C + D + I + V
        2414,2415,2416,2514,2515,2516,2614,2615,2616,    2417,2517,2617,    2418,2518,2518,   1418,1518,1618 , 1724,1725,1726}
        
                                       #I + V + C       
        tres_letras_tres_caracteres = {241,251,261}

                                         #V + C + C + I    #C + D + C + C     #C + V + C + I    #I + D + C + C
        tres_letras_cuatro_caracteres = {4112,5112,6112,        1711,         1412,1512,1612,        2711}

                                                         #C + V + C + C + V                      #C + V + C + C + D 
        tres_letras_cinco_caracteres = {14114,14115,14116,15114,15115,15116,16114,16115,16616,    14117,15117,16117,  24114,24115,24116,25114,25115,25116,26114,26115,26116,  24117,25117,26117,     24118,25118,26118}

                                            #C + V + C + C + I
        cuatro_letras_cinco_caracteres =  {14112,15112,16112, 14112,15112,15112, 24111,25111,26111, 24112,25112,26112, 14111,15111,16111,   17711} 

        count = 0
        while len(segundos_elementos) > 0:

            
            #3 letras 5 Caracteres
            if len(segundos_elementos) >= 5 and int(str(segundos_elementos[0]) + str(segundos_elementos[1]) + str(segundos_elementos[2]) + str(segundos_elementos[3]) + str(segundos_elementos[4])) in tres_letras_cinco_caracteres:
                self.silabas.append(primeros_elementos[0]+primeros_elementos[1]+primeros_elementos[2])
                del segundos_elementos[0:3]
                del primeros_elementos[0:3]        
            
            #4 letras 5 Caracteres
            elif len(segundos_elementos) >= 5 and int(str(segundos_elementos[0]) + str(segundos_elementos[1]) + str(segundos_elementos[2])+ str(segundos_elementos[3])+ str(segundos_elementos[4])) in cuatro_letras_cinco_caracteres:
                self.silabas.append(primeros_elementos[0]+primeros_elementos[1]+primeros_elementos[2]+primeros_elementos[3])
                del primeros_elementos[0:4]
                del segundos_elementos[0:4]

            #2 letras 4 Caracteres
            elif len(segundos_elementos) >= 4 and int(str(segundos_elementos[0]) + str(segundos_elementos[1]) + str(segundos_elementos[2]) + str(segundos_elementos[3])) in dos_letras_cuatro_caracteres:
                self.silabas.append(primeros_elementos[0] + primeros_elementos[1])
                del primeros_elementos[0:2]
                del segundos_elementos[0:2]
    
            #3 letras 4 Carecteres
            elif len(segundos_elementos) >= 4 and int(str(segundos_elementos[0]) + str(segundos_elementos[1]) + str(segundos_elementos[2])+ str(segundos_elementos[3])) in tres_letras_cuatro_caracteres:
                self.silabas.append(primeros_elementos[0]+primeros_elementos[1]+primeros_elementos[2])
                del segundos_elementos[0:3]
                del primeros_elementos[0:3]
            

            #1 Letra 3 Caracteres
            elif len(segundos_elementos) >= 3 and int(str(segundos_elementos[0]) + str(segundos_elementos[1]) + str(segundos_elementos[2])) in una_letra_tres_caracteres:
                self.silabas.append(primeros_elementos[0])
                del segundos_elementos[0:1]
                del primeros_elementos[0:1]
            
            #2 letras 3 Caracteres
            elif len(segundos_elementos) >= 3 and int(str(segundos_elementos[0]) + str(segundos_elementos[1]) + str(segundos_elementos[2])) in dos_letra_tres_caracteres:
                self.silabas.append(primeros_elementos[0] + primeros_elementos[1])
                del primeros_elementos[0:2]
                del segundos_elementos[0:2]
            
            #3 letras 3 Caracteres
            elif len(segundos_elementos) >= 3 and int(str(segundos_elementos[0]) + str(segundos_elementos[1]) + str(segundos_elementos[2])) in tres_letras_tres_caracteres:
                self.silabas.append(primeros_elementos[0]+primeros_elementos[1]+primeros_elementos[2])
                del segundos_elementos[0:3]
                del primeros_elementos[0:3]

            #1 letras 2 caracteres
            elif len(segundos_elementos) >= 2 and int(str(segundos_elementos[0]) + str(segundos_elementos[1])) in una_letra_dos_caracteres:
                self.silabas.append(primeros_elementos[0])
                del segundos_elementos[0:1]
                del primeros_elementos[0:1]

            count += 1
            if count > len(self.word):
                self.silabas.append("".join(primeros_elementos))
                break


while True:
    prueba = separador_silaba(input("Ingresa la palabra en español: "))
    prueba.main()
    print(prueba.tipo_de_letra)
    prueba.separar_silabas()
    print("-".join(prueba.silabas))
    if input("Quiere terminar ya? Y: ") == "Y":
        break
    os.system("cls")
