





#Testing
# Test this
# from random import randint
# import sys
# # generate a number 1~10
# answer = randint(1, 10)
#
# while True:
#     try:
#         guess = int(input('guess a number 1~10:  '))
#         if  0 < guess < 11:
#             if guess == answer:
#                 print('you are a genius!')
#                 break
#         else:
#             print('hey bozo, I said 1~10')
#     except ValueError:
#         print('please enter a number')
#         continue

# # #My answer:
# from random import randint
#
#
# # Function to generate a random number
# def generate_random_number():
#     return randint(1, 10)
#
#
# # Function to check if the guess is valid
# def is_valid_guess(guess):
#     return 0 < guess < 11
#
#
# Function to get user input
# def get_user_guess():
#     try:
#         return int(input('Guess a number 1~10: '))
#     except ValueError:
#         print("Please enter a valid number.")
#         return None
#
#
# # Function to compare the guess with the answer
# def check_guess(guess, answer):
#     if guess == answer:
#         print("You are a genius!")
#         return True
#     else:
#         return False
#
#
# # Main game logic
# def game():
#     answer = generate_random_number()
#
#     while True:
#         guess = get_user_guess()
#
#         if guess is None:  # Invalid input, retry
#             continue
#
#         if is_valid_guess(guess):
#             if check_guess(guess, answer):
#                 break
#         else:
#             print("Hey bozo, I said 1~10!")
#
#
# # To start the game
# if __name__ == "__main__":
#     game()
#
#
#
#











#Regular Expressions


# import re
#
# pattern = re.compile(r"^[a-zA-Z0-9$%&/]{8,}$")
# string = "32sd1fsdv%&"
#
# a = pattern.search(string)
#
# print(a)


# print(a.start())#tells me when the text starts 10
# print(a.end())#tells me when the text ends 13
# print(a.group()) #grives us the matching part "bin"
# #this is useful more multiple searches!
#






#somebody gives you a massive text file, any file, translate this to from de to en
# import argostranslate.package
# import argostranslate.translate
# import os
#
# # Load and install the language package if needed
# argostranslate.package.install_from_path("./app/translate-de_en-1_0.argosmodel")
#
# # Define paths for original and translated files
# original_file_path = "./app/test.txt"
# translated_file_path = "./app/test_translated.txt"
#
# # Read the file and use its content for translation
# with open(original_file_path, mode="r", encoding="utf-8") as my_file:
#     file_content = my_file.read()
#
# # Translate the content of the file from German to English
# translated_text = argostranslate.translate.translate(file_content, "de", "en")
#
# # Create a new file and write the untranslated and translated text into it
# with open(translated_file_path, mode="w", encoding="utf-8") as translated_file:
#     translated_file.write("--- Original Text ---\n")
#     translated_file.write(file_content)
#     translated_file.write("\n\n--- Translated Text ---\n")
#     translated_file.write(translated_text)
#
# # Output the translated text
# print(f"Translated text written to {translated_file_path}")
#




# try:
#     with open("./app/test.txt", mode="r") as my_file:
#         print(text)
# except FileNotFoundError as err:
#     print("file does not exist")
#     raise err
# except IOError as err:
#     print("IO Error")
#     raise err
#
# # my_file = open("test.txt")
# #
# # print(my_file.readlines())
# #
# # my_file.close()
# #
# with open(r"C:\Users\km\Desktop\ViresConferre\Testprogramme\Willisbest\app\app\test.txt", mode="a") as my_file:
#     # Your file operations go here
#
# with open("C:\\Users\\km\\Desktop\\ViresConferre\\Testprogramme\\Willisbest\\app\\app\\test.txt",mode="a") as my_file:
# # Your file operations go here


# import pdb
#
# def add(num1, num2):
#     pdb.set_trace()
#     return num1+num2
#
# add(4,"ffff")
#
#








#modules
# from array import array
#
# array("i", [1,2,3])
#

# import datetime
#
# print(datetime.date.today())


# from collections import Counter, defaultdict, OrderedDict
#
# d1 = OrderedDict()
# d1["a"] = 1
# d1["b"] = 2
#
# d2 = OrderedDict()
# d2["a"] = 2
# d2["b"] = 1
#
# print(d2 == d1)

# li = [1,2,3,4,5,6,7,7]
# sentence = "bla bla skldjbnsadflg"

# dictionary = defaultdict(lambda: "does not exist", {"a":1, "b":2})
# print(dictionary["c"])











#Generators

#def fib(num): # this takes the Index Number of Fibonacci, so F19=4181 and so on
#Its supposed to return all the numbers (using generators) until we get to the index location

# def gen_fun(num):
#     last = 0
#     current = 1
#     for _ in range(num):
#         yield last
#         temp = last
#         last = current
#         current = temp + current
#
# for cunts in gen_fun(20):
#     print(cunts)
#


# def fib(num):
#     return list(gen_fun(num))

# print(fib(19))












# class MyGen():
#     current = 0
#     #This makes it able to use first and last
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#     #This makes us able to iterate through the Object
#     def __iter__(self):
#         return self
#     #We also want to be able to use Next
#     def __next__(self):
#         if MyGen.current < self.last:
#             num = MyGen.current
#             MyGen.current += 1
#             return num
#         raise StopIteration


# gen = MyGen(0,100)
# #Were Looping through the Generator printing each value
# for i in gen:
#     print(i)





# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator)*2)
#         except StopIteration:
#             break

# special_for([1, 2, 3])







# def gen_fun(num):
#     for i in range(num):
#         yield i

# for item in gen_fun(100):
    #...






# from time import time

# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, *kwargs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper

# @performance
# def long_time():
#     print('1')
#     for i in range(100000000): #it finishes after.
#         i*5

# long_time()
# print()

# @performance
# def long_time2():
#     print('2')
#     for i in list(range(100000000)): #it took longer.
#         i*5

# long_time2()
# print()



# def generator_function(num):
#     for i in range(num):
#         yield i*2

# g = generator_function(100)
# next(g)
# next(g)
# print(next(g))
# # for penis in generator_function(1000):
# #     print(penis)


# range(100)
# list(range(100))

# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result

# my_list = make_list(100)
# print(my_list)






















# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)
#         print("woops")

# print(sum("1", 2))





# #Error Handling

# while True:
#     try:
#         age = int(input("what is your age? "))
#         10/age
#         raise ValueError("Hey, cut it out!")

#     except ZeroDivisionError:
#         print("You have to be older than zero")
#     else:
#         print("thank you!")
#         break
#     finally:
#         print("I'm finally done")
#     print("can you hear me?")


# age = int(input("what is your age? "))
# print("your are:", age, "years old!")


















 





# # Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user1 = {
#     'name': 'Sorna',
#     'valid': True #changing this will either run or not run the message_friends function.
# }


# def authenticated(fn):
#     # code here
#     def wrapper(*args, **kwargs):
#         if args[0]["valid"]:
#             return fn(*args, **kwargs)
#         else:
#             return print("invalid user")

#     return wrapper

# @authenticated #  This tells Python to apply the authenticated 
# # function as a decorator to message_friends. 
# def message_friends(user):
#     print('message has been sent')

# message_friends(user1)



# #Decorator
# from time import time
# def performance(fn):
#     def wrapper(*args, **kawrgs):
#         t1 = time()
#         result = fn(*args, **kawrgs)
#         t2 = time()
#         print(f"took {t2-t1} ms")
#         return result
#     return wrapper

# @performance
# def long_time():
#     for i in range(10000000):
#         i*5

# long_time()


# # Decorator
# def logger(fn):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {fn.__name__} with arguments: {args} {kwargs}")
#         result = fn(*args, **kwargs)
#         print(f"{fn.__name__} returned: {result}")
#         return result
#     return wrapper

# @logger
# def add(x, y):
#     return x + y

# @logger
# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"

# # Test the logger decorator
# print(add(5, 10))
# print(greet("Alice"))
# print(greet("Bob", greeting="Hi"))



# class Player:
#     def __init__(self, name, level):
#         self.name = name
#         self.level = level
#         self.exp = 0

#     def gain_exp(self, points):
#         self.exp += points
#         print(f"{self.name} gained {points} experience points!")

#     @staticmethod
#     def calculate_damage(base_damage, weapon_bonus):
#         return base_damage + weapon_bonus

#     @staticmethod
#     def calculate_level_up(current_level, exp_points):
#         return current_level + exp_points // 100

# # Create a player instance
# player1 = Player("Hero", 5)

# # Player gains experience
# player1.gain_exp(120)

# # Calculate damage without needing player-specific info
# damage = Player.calculate_damage(50, 10)
# print(f"Damage dealt: {damage}")

# # Calculate level up based on total experience points
# new_level = Player.calculate_level_up(player1.level, player1.exp)
# print(f"{player1.name} is now at level {new_level}!")













# def my_decorator(func):
#     def wrap_func(*args,**kwargs):
#         print("XXXXXXXXXX")
#         func(*args,**kwargs)
#         print("XXXXXXXXXX")
#     return wrap_func

# @my_decorator
# def hello(greeting, emoji = ":("):
#     print(greeting, emoji)

# hello("hi")











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


