"""
Este módulo se encarga de iniciar el servidor API, cargar la base de datos y agregar los puntos finales.
"""
from flask import Flask, jsonify, request
from datastructure import FamilyStructure

app = Flask(__name__)
jackson_family = FamilyStructure('Jackson')

# Endpoint para obtener todos los miembros de la familia
@app.route('/members', methods=['GET'])
def get_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# Endpoint para recuperar un solo miembro por su ID
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({'error': 'Member not found'}), 404

# Endpoint para agregar un nuevo miembro a la familia
@app.route('/member', methods=['POST'])
def add_member():
    new_member = request.json
    jackson_family.add_member(new_member)
    return jsonify({'message': 'Member added successfully'}), 200

# Endpoint para eliminar un miembro por su ID
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    if jackson_family.delete_member(member_id):
        return jsonify({'message': 'Member deleted successfully'}), 200
    else:
        return jsonify({'error': 'Member not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)