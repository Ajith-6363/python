class animal:
    def sound():
        pass
class pet(animal):
    def bark():
        print("the animal is sounding")
class dog(pet):
    def bark(self):
        print("bow bow bow")
dogish=dog()
print(dogish.bark())