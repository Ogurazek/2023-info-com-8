Frase = input("Ingrese un articulo o frase: ")
letra1 = input("Ingrese la letra 1 a eleccion: ")
letra2 = input("Ingrese la letra 2 a eleccion: ")
letra3 = input("Ingrese la letra 3 a eleccion: ")
#1- Cantidad de veces que aparece cada una de letras que eligió.

texto = Frase.lower()
letras = [letra1.lower(), letra2.lower(), letra3.lower()]
for letra in letras:
    print(f'La letra {letra} aparecio {texto.count(letra)} veces')
    
# 2- Cuantas palabras hay en total en todo el texto.

palabras = Frase.replace("."," ")
palabras = Frase.replace(","," ")
palabras = Frase.replace(":"," ")
palabras = Frase.replace("?"," ")
palabras = Frase.split()
total_de_palabras = len(palabras)
print(f"en la frase hay un total de: {total_de_palabras} palabras")

#3- Cual es la primera letra y cuál es la última. (Indexación)

primer_letra = Frase[0]
ultima_letra = Frase[-1]

print(f"la primera letra de su frase es: {primer_letra}, y la última letra de su frase es {ultima_letra} ")

#4- Mostrar el texto en orden inverso

frase_inverso = Frase[::-1]

print(f"su frase al reves es: {frase_inverso}") 

#5- Decir si la palabra "python" aparece en el texto.

aparece_python = "python" in Frase 
palabra_python = {True: "la palabra python aparece en tu frase",
                  False: "la palabra python no aparece en tu frase"}
print(palabra_python[aparece_python])
