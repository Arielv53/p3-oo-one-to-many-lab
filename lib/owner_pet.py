class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        pets = self.pets()
        if not all(isinstance(pet, Pet) for pet in pets):
            raise Exception("All pets must be instances of the Pet class")
        return sorted(pets, key=lambda pet: pet.name)