
class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def actuar(self):
        print(f"🎶 {self.nombre} canta su éxito '{self.cancion_mas_popular}' con gran energía.")

class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo

    def actuar(self):
        print(f" El DJ {self.nombre} mezcla temas de estilo {self.estilo}, haciendo vibrar al público.")

class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes

    def actuar(self):
        print(f" La banda {self.nombre} con {self.integrantes} integrantes toca un poderoso solo de guitarra.")
