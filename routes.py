from flask import Blueprint, jsonify, request
from character_manager import CharacterManager


character_bp = Blueprint('characters', __name__)
#es una forma de organizar rutas en modulos, permite separa en archivos mas limpios. Flask lo reconoce.
#characters es el nombre que le doy al blueprint y el __name__ es lo que le dice a Flask donde fue creado y su contenido
#bluprint pieza de lego, app.py es el tablero donde armas y el __name__ es una etiqueta interna que le dice al tablero donde esta y como usarla.


#characters = [
#            {
#                'id': 1,
#                'name': 'Gandalf',
#                'quote': 'A wizard is never late, nor is he early. He arrives precisely when he means to.'
#            },
#            {
#                'id': 2,
#                'name': 'Frodo Baggins',
#                'quote': 'I will take the Ring to Mordor. Though… I do not know the way.'
#            },
#        ]
#character_id_counter = 3

manager = CharacterManager()


#@decorador, asocia la ruta a una funcion. cuando se hace la peticion a la ruta con el metodo, automaticamente ejecuta la funcion definida.
@character_bp.route('/characters', methods=["GET"])
def get_characters():
    characters = manager.get_all()
    return jsonify(characters), 200

#ahora en el app hago lo del blueprint para que sepa de el
#introduccion a postman


@character_bp.route('/characters/<int:char_id>', methods=["GET"])
def get_character(char_id):
    #for character in characters:
    #    if character["id"] == char_id:
    #        return jsonify(character), 200
    #return jsonify({"error": "Character not found"}),400
    character = manager.get(char_id)
    if character:
        return jsonify(character), 200
    return jsonify({"error": "Character not found"}), 404


@character_bp.route('/characters', methods=["POST"])
def create_character():
    data = request.get_json()
#para postman "name": "Aragorn", "quote": "If by my life or death I can protect you. I will."
    required_fields = ["name", "quote"]
    missing = [field for field in required_fields if field not in data]
    if missing: 
        return jsonify({"error": f'Missing fields: {missing}'}), 404
    #solo por estar trabajando aca necesito acceder a la variable arriba global, de lo contrario da un error como si creara una nueva variable
    #global character_id_counter
    #new_character = {
    # "id": character_id_counter,
    # "name": data["name"],
    # "quote": data["quote"]
    #}
    #characters.append(new_character)
    #character_id_counter += 1

    #esto no por ahora
    new_character = manager.create(data)
    
    return jsonify(new_character), 201

@character_bp.route('/characters/<int:char_id>', methods=['PUT'])
def update_character(char_id):
    data = request.get_json()
#    for character in characters:
#        if character["id] == char_id:
#            charcter["name"] = data.get("name", character["name"])
#            charcter["quote"] = data.get("quote", character["quote"])
#            return jsonify(character), 200
#    return jsonify({"error": "Character not found"}), 400

    
    #esto no va por ahora
    character = manager.update(char_id, data)
    if character:
        return jsonify(character), 200
    return jsonify({'error': 'Character not found'}), 404

@character_bp.route('/characters/<int:char_id>', methods=["DELETE"])
def delete_character(char_id):
    if manager.delete(char_id):
        return jsonify({"msg": " Character deleted"}), 200
    return jsonify({"error": "Character not found"}), 404
