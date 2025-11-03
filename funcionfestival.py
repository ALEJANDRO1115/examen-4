
def iniciar_festival(lista_artistas):
    print("\n ¡Bienvenidos al Festival de Música! \n")
    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("Fin de la actuación \n")
