# PEP 8 como definir los nombres segun lo que representa
#resumen rapido:
#tipo de cosa               Convencion de nombres           Ejemplo
#Clases                     PascalCase                      CharacterManager
#Funciones o variables      snake_case                      character_manager

class CharacterManager:
    #constructor
    def __init__(self):
        self._characters = [
            #Guion abajo en POO existe encapsulamiento son elementos que solo pdeberias acceder a traves de metodos
            #son propiedades que queremos aislar para que no sean modificados de otra forma distinta al metodo.
            #python no tiene encapsulamiento forzado. por tanto por convencion usamos el _ para indicar que lo estamos encapsulando
            #le dice q otros desarrolladores que no deberian modificarlos sin un metodo.
            
            {
                'id': 1,
                'name': 'Gandalf',
                'quote': 'A wizard is never late, nor is he early. He arrives precisely when he means to.'
            },
            {
                'id': 2,
                'name': 'Frodo Baggins',
                'quote': 'I will take the Ring to Mordor. Though… I do not know the way.'
            },
        ]
        self._next_id = 3

    def get_all(self):
        return self._characters

    def get(self, char_id):
        for character in self._characters:
            if character["id"] == char_id:
                return character
        return None

    def create(self, data):
        character = {
            "name": data["name"],
            "quote": data["quote"],
            "id": self._next_id
        }
        self._characters.append(character)
        self._next_id += 1
        return character

    def update(self, char_id ,data):
        character = self.get(char_id)
        if character:
            character["name"] = data.get("name", character["name"])
            character["quote"] = data.get("quote", character["quote"])
        return character

    def delete(self, char_id):
        character = self.get(char_id)
        if character:
            self._characters.remove(character)
            return True
        return False
