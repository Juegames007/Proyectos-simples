
class separador_silaba:
    consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"] #!
    grupo_consonante_no_separar = ["pl", "pr", "bl", "br", "cl", "cr", "fl", "fr", "gl", "gr", "dr", "tr", "ch", "ll", "rr"] #2
    vocales = ["a","e","i","o","u","á","é","í","ó","ú"] #3
    vocales_abiertas = ["a","e","o","á","é","ó"] #4
    vocales_cerradas = ["i","u"] #5
    vocales_cerradas_tilde = ["í","ú"] #6
    diptongo = ["ai","au","ei","eu","ia","ie","io","iu","oi","ou","ua","ue","ui","uo"] #7
    hiato = ["aa","aá","áa","ae","áe","aé","aí","ao","áo","aó","aú","ea","éa","eá","ee","ée","eé","eí","eo","éo","eó","eú",
             "ía","ié","íu","oa","óa","oá","oe","óe","oé","oí","oo","óo","oó","oú","úa","úe","úo"] #8
    
    def __init__(self,word):
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
        primeros_elementos = [x[0] for x in self.tipo_de_letra]
        segundos_elementos = [x[1] for x in self.tipo_de_letra] 
        vocal_cons_vocal = {414,415,416,514,515,516,614,615,616}                              #conso + vocal + conso + conso + diptongo
        cons_vocal_cons_cons_vocal = {14114,14115,14116,15114,15115,15116,16114,16115,16616,            14117,15117,16117}
        cons_dipton_cons_vocal = {1714,1715,1716,  1724,1725,1726} 
        inseparable_vocal_conson = {241,251,261}
        vocal_cons_cons_insepara = {4112,5112,6112}                             #vocal + cons + cons + diptongo         #vocal + cons + inseparable + vocal        #vocal + cons + inseparable + diptongo
        vocal_cons_cons_vocal = {4114,4115,4115,5114,5115,5116,6114,6115,6116,         4117,5117,6117,               4124,4125,4126,5124,5125,5126,6124,6125,6126,          4127,5127,6127 }

                                                                               #conso + vocal + conso + diptongo   #conso + diptongo + conso + vocal
        cons_vocal_cons_vocal = {1414,1415,1416,1514,1515,1516,1614,1615,1616,         1417,1517,1617,                  2714,2715,2716 }
        cons_hiato_hiato_cons = {1841,1851,1861}
        cons_vocal_cons_cons_inseparable = {14112,15113,16114}

        count = 0
        while len(segundos_elementos) > 0:

            #vocal + consonante + vocal
            if len(segundos_elementos) >= 3 and int(str(segundos_elementos[0]) + str(segundos_elementos[1]) + str(segundos_elementos[2])) in vocal_cons_vocal:
                self.silabas.append(primeros_elementos[0])
                del segundos_elementos[0:1]
                del primeros_elementos[0:1]
            
            #consonante + vocal + consonante + consonante + vocal
            elif len(segundos_elementos) >= 5 and int(str(segundos_elementos[0]) + str(segundos_elementos[1]) + str(segundos_elementos[2]) + str(segundos_elementos[3])+str(segundos_elementos[4])) in cons_vocal_cons_cons_vocal:
                self.silabas.append(primeros_elementos[0]+primeros_elementos[1]+primeros_elementos[2])
                del segundos_elementos[0:3]
                del primeros_elementos[0:3]
            
            #vocal + consonante + consonante + inseparable 
            elif len(segundos_elementos) >= 4 and int(str(segundos_elementos[0]) + str(segundos_elementos[1]) + str(segundos_elementos[2]) + str(segundos_elementos[3])) in vocal_cons_cons_insepara:
                self.silabas.append(primeros_elementos[0]+primeros_elementos[1]+primeros_elementos[2])
                del primeros_elementos[0:3]
                del segundos_elementos[0:3]

            #inseparable + vocal + consonante
            elif len(segundos_elementos) >= 3 and int(str(segundos_elementos[0]) + str(segundos_elementos[1]) + str(segundos_elementos[2])) in inseparable_vocal_conson:
                self.silabas.append(primeros_elementos[0]+primeros_elementos[1]+primeros_elementos[2])
                del primeros_elementos[0:3]
                del segundos_elementos[0:3]

            #vocal + constante + constante + vocal
            elif len(segundos_elementos) >= 4 and int(str(segundos_elementos[0]) + str(segundos_elementos[1]) + str(segundos_elementos[2]) + str(segundos_elementos[3])) in vocal_cons_cons_vocal:
                self.silabas.append(primeros_elementos[0] + primeros_elementos[1])
                del primeros_elementos[0:2]
                del segundos_elementos[0:2]

            #consonante + vocal + consonante + vocal
            elif len(segundos_elementos) >= 4 and int(str(segundos_elementos[0]) + str(segundos_elementos[1]) + str(segundos_elementos[2]) + str(segundos_elementos[3])) in cons_vocal_cons_vocal:
                self.silabas.append(primeros_elementos[0] + primeros_elementos[1])
                del primeros_elementos[0:2]
                del segundos_elementos[0:2]
            
            #consonante + diptongo + consonante + vocal
            elif len(segundos_elementos) >= 4 and int(str(segundos_elementos[0]) + str(segundos_elementos[1]) + str(segundos_elementos[2]) + str(segundos_elementos[3])) in cons_dipton_cons_vocal:
                self.silabas.append(primeros_elementos[0]+primeros_elementos[1])
                del primeros_elementos[0:2]
                del segundos_elementos[0:2]
            
            #consonante + hiato + hiato + consonante
            elif len(segundos_elementos) >= 4 and int(str(segundos_elementos[0]) + str(segundos_elementos[1]) + str(segundos_elementos[2])+ str(segundos_elementos[3])) in cons_hiato_hiato_cons:

                self.silabas.append(primeros_elementos[0]+primeros_elementos[1])
                print(primeros_elementos)
                del primeros_elementos[0:2]
                del segundos_elementos[0:2]
                print(primeros_elementos)
            
            #consonante + vocal + consonante + consonante + inseparable
            elif len(segundos_elementos) >= 5 and int(str(segundos_elementos[0]) + str(segundos_elementos[1]) + str(segundos_elementos[2])+ str(segundos_elementos[3])+ str(segundos_elementos[4])) in cons_vocal_cons_cons_inseparable:
                self.silabas.append(primeros_elementos[0]+primeros_elementos[1]+primeros_elementos[2]+primeros_elementos[3])
                print(primeros_elementos)
                del primeros_elementos[0:4]
                del segundos_elementos[0:4]
                print(primeros_elementos)

        
            count += 1
            if count > 40:
                self.silabas.append("".join(primeros_elementos))
                break



prueba = separador_silaba("incluido")
prueba.main()
print(prueba.tipo_de_letra)
prueba.separar_silabas()
print(prueba.silabas)
                
                