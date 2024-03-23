class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.__class__.all.append(self)
class Owner:
    def __init__(self, name, pets=None):
        self.name = name
        self.pets_list = []
        if pets is not None:
            for pet in pets:
                self.add_pet(pet)

    def pets(self):
        return self.pets_list

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Not a Pet instance")
        pet.owner = self
        self.pets_list.append(pet)

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets_list, key=lambda x: x.name)
        return sorted_pets

