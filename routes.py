from flask import Blueprint, jsonify, request
from character_manager import CharacterManager


character_bp = Blueprint('characters', __name__)

manager = CharacterManager()



@character_bp.route('/characters', methods=["GET"])
def get_characters():
    characters = manager.get_all()
    return jsonify(characters), 200


@character_bp.route('/characters/<int:char_id>', methods=["GET"])
def get_character(char_id):
    character = manager.get(char_id)
    if character:
        return jsonify(character), 200
    return jsonify({"error": "Character not found"}), 404


@character_bp.route('/characters', methods=["POST"])
def create_character():
    data = request.get_json()

    required_fields = ["name", "quote"]
    missing = [field for field in required_fields if field not in data]
    if missing: 
        return jsonify({"error": f'Missing fields: {missing}'}), 404

    new_character = manager.create(data)
    
    return jsonify(new_character), 201

@character_bp.route('/characters/<int:char_id>', methods=['PUT'])
def update_character(char_id):
    data = request.get_json()
    character = manager.update(char_id, data)
    if character:
        return jsonify(character), 200
    return jsonify({'error': 'Character not found'}), 404

@character_bp.route('/characters/<int:char_id>', methods=["DELETE"])
def delete_character(char_id):
    if manager.delete(char_id):
        return jsonify({"msg": " Character deleted"}), 200
    return jsonify({"error": "Character not found"}), 404