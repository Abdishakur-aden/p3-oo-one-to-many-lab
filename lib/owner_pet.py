class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.owner = owner
        if pet_type not in Pet.PET_TYPES:
            raise Exception (f"{pet_type} is not a valid pet type")
        self.pet_type = pet_type
        Pet.all.append(self)





class Owner:
    def __init__(self, name):
        self.name = name

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception(f"{pet} is not a valid pet")
        pet.owner = self

    def pets(self):
        return Pet.all
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key= lambda pet: pet.name)
