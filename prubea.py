palabra_secreta = "Haolaaaaa"
length = len(palabra_secreta)
letra = "a"

lista = [i for i in range(length) if palabra_secreta[i] == letra]
print(lista)