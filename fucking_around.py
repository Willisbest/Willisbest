class Shelter():
    def __init__(self, animals):
        self.animals = animals
      
    def adopt_all(self):
        for animal in self.animals:
            print(animal.adopt())

    def bark_all(self):
        for animal in self.animals:
            print(animal.bark())
    
        
class Dog():
    is_a_good_boi = True
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def adopt(self):
        return f"{self.name} has been adopted"
    

class Bulldog(Dog):
    def bark(self, sound="WOOOF!"):
        return f"{self.name}, the {self.__class__.__name__} barks: {sound}"

class Beagle(Dog):
    def bark(self, sound="woof..."):
        return f"{self.name}, the {self.__class__.__name__} barks: {sound}"

class Chiuaua(Dog):
    def bark(self, sound="mimimimimiiiii"):
        return f"{self.name}, the {self.__class__.__name__} barks: {sound}"


abandoned_dogs = [Bulldog("Jürgen", 1), Beagle("Hans", 2), Chiuaua("Hasnat", 3)]


saved_dogs = Shelter(abandoned_dogs)

#saved_dogs.adopt_all()
saved_dogs.bark_all()
