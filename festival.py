
# Clase base
class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def presentarse(self):
        print(f"🎤 Hola, soy {self.nombre} y mi género es {self.genero}.")

    def actuar(self):
        print(" Estoy actuando en el escenario...")

    def despedirse(self):
        print(f" Gracias por escuchar a {self.nombre}.\n")
