
class silaba:
    consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    grupo_consonante_no_separar = ["pl", "pr", "bl", "br", "cl", "cr", "fl", "fr", "gl", "gr", "dr", "tr", "ch", "ll", "rr"]

    def __init__(self,word):
        self.word = word
    def separar_por_silabas(self):
        palabra_separada = []
        for indice,letter in enumerate(self.word):
            if not (None in palabra_separada[indice]):
                palabra_separada[indice] += letter
                for letra in palabra_separada[indice]:
                    if letra in self.consonantes:
                        pass
            else:
                palabra_separada.append(letter)

class hiato:
    def __init__(self, word):
        self.word = word
class triptongo:
    def __init__(self, word):
        self.word =word

