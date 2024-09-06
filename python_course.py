




break










# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def run(self):
        print("run")
# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Maunzi", 3)
cat2 = Cat("Maunschi", 2)
cat3 = Cat("Marschi", 7)
print(cat1, cat2, cat3)

# 2 Create a function that finds the oldest cat

#My ugly solution
# def oldest_whatever(*args):
#     if cat1.age > cat2.age and cat1.age > cat3.age:
#         oldest_cat = cat1
#         print("Cat1 is the oldest cat!")
#     if cat2.age > cat1.age and cat2.age > cat3.age:
#         oldest_cat = cat2
#         print("Cat2 is the oldest cat!")
#     if cat3.age > cat1.age and cat3.age > cat2.age:
#         oldest_cat = cat3
#         print("Cat3 is the oldest cat!")
#     return oldest_cat

#Chat GPT
def find_oldest_cat(cat_list):
    oldest_cat = max(cat_list, key=lambda x: x.age)
    print(f"The oldest cat is {oldest_cat.name} who is {oldest_cat.age} years old!")
    print("Congratulations!")
    print("""
       /\_/\  
      ( o.o ) 
       > ^ <  
    """)
# Instantiate the Cat object with 3 cats
cat1 = Cat("Maunzi", 3)
cat2 = Cat("Maunschi", 2)
cat3 = Cat("Marschi", 7)

# Find the oldest cat
find_oldest_cat([cat1, cat2, cat3])

# class PlayerCharacter:
#     membership = True               #Class Object Attribute, they are fix for all objects while the others are flexible
#     def __init__(self, name, age):  #init method, its a special method
#         if (self.membership):       #
#             self.name = name        #these are attributes
#                                     #self refers to the PlacerCharacter, can also be named this way
#             self.age = age

#     def run (self, hello):                 #with their own methods as well
#         print('run')
#         return 'done'

# player1 = PlayerCharacter('Karl', 27)
# player2 = PlayerCharacter('Sage', 23)
# player2.attack = 50                 #Attributes can also be assigned to create our own objects
# print(player1.run('hello'))
# print(player2.attack)
# print(player1.)

# my_string = "Hello, World!"
# new_string = my_string.replace("World", "Universe")
# print(new_string)  # Output will be "Hello, Universe!"

# print(type(1'''this is meant to be an example datatype that is very short'''))

# a = 1


# def parent():
#     a = 10

#     def confusion():
#         return a
#     return confusion()


# print(parent())
# print(a)


# a ='peniss'
# if ((n := len(a)) >5):
#     print(f'too long {n} elements')
# while ((n := len(a)) > 1):
#     print(n)
#     a = a[:-1]

# # even_numbers.append(1)

# def highest_even(li):
#     even_numbers = []
#     for num in li:
#         if num % 2 == 0:
#             even_numbers.append(num)
#     return max(even_numbers)


# print(highest_even([11, 2, 3, 6, 7, 10]))

# print(even_numbers)


# Find the highest even number


# def is_dick(name, *args, i='hi', **kwargs):
#     total = 0
#     for items in kwargs.values():
#         total += items
#     return sum(args) + total

# print(is_dick('Andy',1,2,3,4,5, num1=5, num2=10))

# Rule: Parameters, *args, Default Parameters, **kwargs

# def checkDriverAge(age=0):
#     '''
#     This function tests for drivers age, it was a test.
#     '''
#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!")
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")
#     age = input("What is your age?: ")


# checkDriverAge(age=92)


# 1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

# 2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
# checkDriverAge(92);
# it returns "Powering On. Enjoy the ride!"
# also make it so that the default age is set to 0 if no argument is given.


# # Parameters
# def say_hello(name, emoji):
#     print (f'helooooooooooo {name}, ich habe dich vermisst {emoji}')

# #Arguments
# say_hello(name='penis', emoji=':)')


# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]

# def show_tree():
#     for row in picture:
#         for pixel in row:
#             if pixel == 0:
#                 print(' ', end='')  # Replace 0 with space
#             elif pixel == 1:
#                 print('*', end='')  # Replace 1 with asterisk
#         print()  # Move to the next row after processing all columns

# show_tree()


# def say_hello():
#     print ('helooooooooooo')

# say_hello()


# some_list = ['a','b','c','b','d','m','n','n']

# some_list.sort()

# #print(some_list)
# previous_letter = ''

# for letter in some_list:
#     if letter == previous_letter:
#         print (letter)
#     previous_letter = letter

# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]

# for row in picture:
#     for pixel in row:
#         if pixel == 0:
#             print(' ', end='')  # Replace 0 with space
#         elif pixel == 1:
#             print('*', end='')  # Replace 1 with asterisk
#     print()  # Move to the next row after processing all columns


# i = 0
# value = 0
# if value in picture is 0:
#     print(' ')
# else:
#     print('*')


# while True:
#     response = input ('du hure!')
#     break


# i = 0
# while i <50:
#     print(i)
#     i+=1
#     break
# else:
#     print('done with all the work)')


# for i,char in enumerate(list(range(100))):
#     if char == 50:
#         print (f'the index of 50 is: {i}')


# for penis in range(0,100, ):
#     print(penis)


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# counter = 0


# for items in my_list:
#     counter = counter + items

# print(counter)


# follower = {
#     'Name': 'Jürgen',
#     'Alter': 55,
#     'can_grill': True
# }

# for x_key, y_value in follower.items():
#     print(x_key, y_value)

# for sextoys in ('dickö', 'taschenmuschi', 'dildo'):
#     for sexsuechtige in ('kitkat','Berghain'):
#         print(sextoys, sexsuechtige)


# is_magician = False
# is_expert = True

# if is_magician and is_expert:
#     print("you are a master magician")
# elif is_magician:
#     print("at least youre getting there")
# else:
#     print("you need magical powers")


# is_huge = True

# groeße_schwanz = "Der ist sehr groß" if is_huge else "Watn Kleiner!"

# print(groeße_schwanz)

# is_old = True
# is_stylish_enough = True
# is_on_guestlist = False
# if is_old and is_stylish_enough:
#     print ('you may go in')
# #print('Dont wanna go to jail')
# elif is_on_guestlist:
#     print("hello there, go in")
# else:
#     print('no way!')


# #Scroll to bottom to see solution
# # You are working for the school Principal. We have a database of school students:
# school = {'Bobby','Tammy','Jammy','Sally','Danny'}

# #during class, the teachers take attendance and compile it into a list.
# attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']
# print(school.difference(attendance_list))


# my_set = {313,456,654}
# your_set = {456,654}

# print(my_set.difference(your_set))


# def multiply_by_two(num):
#     return num*2


# def sum(num1, num2):
#     return num1+num2


# print(sum(20, 3))

# print('Helooooo du penis')
