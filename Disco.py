class Disco:
    def __init__(self,peso):
        self._peso = peso


    def get_peso(self):
        return self._peso


    def to_string_disco(self):
        print(self._peso)