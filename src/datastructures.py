
"""
actualice este archivo para implementar los siguientes métodos ya declarados:
- add_member: debe agregar un miembro a la lista self._members
- eliminar_miembro: debe eliminar un miembro de la lista self._members
- update_member: debe actualizar un miembro de la lista self._members
- get_member: debe devolver un miembro de la lista self._members
"""
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        member["id"] = self._generate_id()
        self._members.append(member)

    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                del self._members[i]
                return True
        return False

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        return self._members