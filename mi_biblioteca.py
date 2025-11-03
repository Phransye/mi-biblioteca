# === mi biblioteca personal ===

# se crea la lista vacía para meter los libros
biblioteca = []  # --> vacia

# se ingresan los libros iniciales
biblioteca.append({"titulo": "Chika Sagawa", "autor": "Chika Sagawa", "anio": "1936"})
biblioteca.append({"titulo": "Lo que nos pasó cuando fuimos niños y qué hicimos con eso", "autor": "Laura Gutman", "anio": "2005"})
biblioteca.append({"titulo": "La hija de la fortuna", "autor": "Isabel Allende", "anio": "1999"})

# tupla de categorías
categorias = ("poesía", "psicología", "novela histórica")

# bucle principal para validar las respuestas e ir imprimiendo los libros
while True:
# va mostrando la lista actualizada
    print("\n=== mi biblioteca ===")
    for indice, libro in enumerate(biblioteca, start=1):
        print(f"{indice}. {libro['titulo']} - {libro['autor']} ({libro['anio']})")
    
    print("\ncategorías disponibles:", categorias)

# pregunta si desea agregar un nuevo libro
    respuesta = input("\n agregamos otro libro a la lista??(s/n): ")

    if respuesta.lower() in ("s", "si", "ok", "bueno", "ya"): #en caso de cualquier opcion parecida a un si
        nuevo_titulo = input("título: ")
        nuevo_autor = input("autor: ")
        nuevo_anio = input("año: ")

        biblioteca.append({"titulo": nuevo_titulo,"autor": nuevo_autor,"anio": nuevo_anio})

        print("\n✅ listo, libro agregadoooo!")

    elif respuesta.lower() in ("n", "no"): #en caso que ponga que no 
        print("\n📚 muchas gracias por usar este sistema, ahi te ves!")
        break

    else:
        print("\n⚠️ haz las cosas bien 👊 (s/n)") #mensajito para el usuario <3