class SuperList():
    def __len__(self):
        return 1000
    pass






# class Toy():
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#         self.my_dict = {
#             'name':'Yoyo',
#             'has_pets': False,
#         }

#     def __str__(self):
#         return f"{self.color}"

#     def __len__(self):
#         return 5

#     def __del__(self):
#         return "deleted"

#     def __call__(self):
#         return('yes??')

#     def __getitem__(self,i):
#         return self.my_dict[i]

#     # 1. __eq__ method to compare equality
#     def __eq__(self, other):
#         return self.color == other.color and self.age == other.age

#     # 2. __add__ method to add two Toy objects
#     def __add__(self, other):
#         return self.age + other.age

#     # 3. __repr__ method for developer-friendly representation
#     def __repr__(self):
#         return f"Toy(color={self.color}, age={self.age})"

# # Testing the dunder methods
# toy1 = Toy('red', 3)
# toy2 = Toy('blue', 5)
# toy3 = Toy('red', 3)

# # __eq__ - Check if two toys are equal
# print(toy1 == toy3)  # True because color and age are the same
# print(toy1 == toy2)  # False because color and age differ

# # __add__ - Add the ages of two toys
# print(toy1 + toy2)  # Outputs: 8 (3 + 5)

# # __repr__ - Developer-friendly representation of the toy
# print(repr(toy1))  # Outputs: Toy(color=red, age=3)

# class User:
#     def __init__(self, email):
#         self.email = email
    
#     def sign_in(self): #no need for __init__ without variables or attributes
#         print("logged")
 
# class Wizard(User):
#     def __init__(self, name, power, email):
#         super().__init__(email)
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f"attacking with the power of {self.power}")

# class Archer():
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f"attacking with arrows: arrows left now: {self.num_arrows}")


# wizard1 = Wizard("merlin", "fire", "emailsmail@gmail.com")

# print(dir(wizard1.email))

# archer1 = Archer("Legolas", 20)

# def player_attack(char):
#     char.attack()

# player_attack(wizard1)
# player_attack(archer1)

# wizard1 = Wizard("merlin", "fire")
# print(isinstance(wizard1, User))

# wizard1 = Wizard("merlin", "fire")
# archer1 = Archer("Legolas", 20)

# wizard1.attack()
# archer1.attack()











# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# #1 Add nother Cat
# class Soeren(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
# #2 Create a list of all of the pets (create 3 cat instances from the above)
# my_cats = [Simon("Simon", 5), Sally("Sally", 4), Soeren("Soeren", 3)]

# #3 Instantiate the Pet class with all your cats use variable my_pets

# my_pets = Pets(my_cats)


# #4 Output all of the cats walking using the my_pets instance

# my_pets.walk()



















# class PlayerCharacter:
#     def __init__(self, name, age):
#         self._name = name           #The underscore in _name means its supposed to be private
#         self._age = age             #Its a signal for other devs but doesnt do anything

#     def run(self):
#         print("run")

#     def speak(self):
#         return print(f"my name is {self._name}, and I am {self._age} years old!")

# player1 = PlayerCharacter("Karl", 28)

# player1.name = "XXX"
# player1.speak = "Boooo"

# print(player1.speak)


