
def main() cantante.py dj.py banda.py functionfestival.py
    lista_artistas = []
    cantidad = int(input("¿Cuántos artistas se presentarán? "))

    for i in range(cantidad):
        print(f"\n Artista {i+1}")
        tipo = input("Tipo de artista (Cantante, DJ o Banda): ").strip().lower()
        nombre = input("Nombre del artista: ")
        genero = input("Género musical: ")
        popularidad = int(input("Popularidad (1-100): "))

        if tipo == "cantante":
            cancion = input("Canción más popular: ")
            artista = Cantante(nombre, genero, popularidad, cancion)
        elif tipo == "dj":
            estilo = input("Estilo musical: ")
            artista = DJ(nombre, genero, popularidad, estilo)
        elif tipo == "banda":
            integrantes = int(input("Número de integrantes: "))
            artista = Banda(nombre, genero, popularidad, integrantes)
        else:
            print("Tipo de artista no válido. Intenta de nuevo.")
            continue

        lista_artistas.append(artista)

    iniciar_festival(lista_artistas)

if __name__ == "__main__":
    main()
