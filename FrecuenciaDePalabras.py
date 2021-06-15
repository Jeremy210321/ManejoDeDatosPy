def abrirLeertxt():
    try:
        archivo = open("Book_4_The_Goblet_of_Fire.txt", encoding='utf-8')
        texto = archivo.read()
        quitar = ',;.-¿”!“¡()—:/?\n|\t"'
        print("\t\t\tFRECUENCIA DE PALABRAS EN UN ARCHIVO .txt\n")
        for caracter in quitar:
            texto = texto.replace(caracter, "")

        texto = texto.lower()
        palabras = texto.split(" ")
        frecuencias = {}
        for palabra in palabras:
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1
        for palabra in frecuencias:
            frecuencia = frecuencias[palabra]
            print(f"({palabra},{frecuencia})")

    except FileNotFoundError:
        msg="Existe un problema con el archivo"
        print(msg)
abrirLeertxt()




