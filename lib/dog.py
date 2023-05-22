#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]
class Dog:
    def __init__(self, name="Mutt", breed=None):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value == "" or len(value) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self.__name = value

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, value):
        if value is not None and value not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self.__breed = value
def main():
    fido = Dog()
    fido.name = "Fido"
    fido.breed = "Human"
    
    print(fido.name)

main()    


#class Dog:
   #def __init__(self, name ="Mutt", breed=None):
        #self.breed = breed

        #if not isinstance(name, str) or name == "" or len(name) > 25:
            #print("Name must be string between 1 and 25 characters.")
        #else:
            #self.name = name   

        #if breed is not None and breed not in APPROVED_BREEDS:
            #print("Breed must be in list of approved breeds.")

#fido = Dog(name="Fido")
#fido = Dog(breed="Human")