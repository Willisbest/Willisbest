def my_decorator(func):
    def wrap_func(*args,**kwargs):
        print("XXXXXXXXXX")
        func(*args,**kwargs)
        print("XXXXXXXXXX")
    return wrap_func

@my_decorator
def hello(greeting, emoji = ":("):
    print(greeting, emoji)

hello("hi")











# return the duplicates "b" and "n" in a list

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# my_task_dict = {}

# #my_task_dict = {letter for letter in some_list if letter != my_task_dict.keys()}
# #my_task_dict = {k: v for k, v in some_list if v != some_list.key}
# #my_task_dict = {letter:letter for letter in [some_list]}
# my_task_dict = {letter for letter in some_list if some_list.count(letter) > 1}



# # duplicates = []
# # for value in some_list:
# #     if some_list.count(value) > 1:
# #         if value not in duplicates:
# #             duplicates.append(value)

# # print(duplicates)
# print(type(my_task_dict))
# print(my_task_dict)











# my_dict = {num:num*2 for num in [1,2,3]}

# print(my_dict)  







# my_list = {char for char in "herllo"}
# my_list2 = {num for num in range(0,100)}
# my_list3 = {num**2 for num in range(0,100)}
# my_list4 = {num**2 for num in range(0,100) if num % 2 ==0}

# print(my_list4)



# my_list = []

# for char in "hello":
#     my_list.append(char)

# print (my_list)










 #lambda practicetasks
# #Sqare it using lambda
# my_list = [5,4,3]

# new_list = list(map(lambda item: item*item, my_list))

# print(new_list)

# #sort list where second value is smallest first and largest last using lambda
# a= [(0,2),(4,3),(10,-1),(9,9)]
# a.sort(key=lambda x: x[1])
# print(a)









# lambda expressions
# lambda param: action(param)


# from functools import reduce

# my_list = [1,2,3]

# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item

# print(reduce(accumulator, my_list, 0))
# print(my_list)









#Exercise for the functions
# from functools import reduce

# # #1 Capitalize all of the pet names and print the list
# # my_pets = ['sisi', 'bibi', 'titi', 'carla']

# # # def capitalize_pet(pet):
# # #     return pet.capitalize()

# # print(list(map(str.capitalize, my_pets)))


# #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# # my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]

# # # my_numbers.sort()

# # print(list(zip(sorted(my_numbers), my_strings)))

# #3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]

# # def over_50(num):
# #     if (num>50):
# #         return num
        
# #print(sorted(list(filter(over_50, scores))))


# #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

# def accumulator(acc, item):
#     return acc + item

# print(reduce(accumulator, scores + my_numbers, 0))
# print(sum(my_numbers+scores))







# from functools import reduce

# my_list = [1,2,3]

# def multiply_by2(item):
#     return item * 2

# def only_odd(item):
#     return item % 2 != 0 #If the remeinder of x/2 does not equal 0 its not odd

# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item

# print(reduce(accumulator, my_list, 0))
# print(my_list)











# my_list = [1,2,3]
# your_list = [10, 20, 30]
# # def multiply_by2(item):
# #     return item * 2

# # def only_odd(item):
# #     return item % 2 != 0 #If the remeinder of x/2 does not equal 0 its not odd

# print(list(zip(my_list, your_list)))
# print(my_list)










# class A:
#     num = 10

# class B(A):
#     pass

# class C(A):
#     num = 1

# class D (B, C):
#     pass

# print(D.mro())
# print(D.num)


#     #     A
#     #   /   \
#     #  /     \
#     # B       C
#     #  \     /
#     #   \   /
#     #     D










# #Multiple Inheritance
# class User:

#     def sign_in(self): #no need for __init__ without variables or attributes
#         print("logged")
 
# class Wizard(User):
#     def __init__(self, name, power):
#         #super().__init__(email)
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

#     def run(self):
#         print(f"{self.name} is running really fast!")


# class HybridBorg(Wizard, Archer):
#     def __init__(self, name, power, num_arrows):
#         Archer.__init__(self, name, num_arrows)
#         Wizard.__init__(self, name, power)

# hb1 = HybridBorg("borgsen", "fire" , 100)

# print(hb1.sign_in())












# class SuperList(list):
#     def __len__(self):
#         return 1000
    
# super_list1 = SuperList();

# print(len(super_list1))
# super_list1.append(5)
# print(super_list1[0])

# print(issubclass(SuperList, list))
# print(issubclass(list, object))



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


