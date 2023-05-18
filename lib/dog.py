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
   def __init__(self, name ="Mutt", breed=None):
        self.breed = breed

        if not isinstance(name, str) or name == "" or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name   

        if breed is not None and breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")

fido = Dog(name="Fido")
fido = Dog(breed="Human")