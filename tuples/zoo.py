'''
Create a tuple named zoo that contains 10 of your favorite animals.
Find one of your animals using the tuple.index(value) syntax on the tuple.
# Example
flowers = ("daisy", "rose")
flower.index("rose") # Output is 1
Determine if an animal is in your tuple by using value in tuple syntax.
animal_to_find = "kangaroo"
if animal_to_find in zoo:
    # Print that the animal was found
You can reverse engineer (unpack) a tuple into another tuple with the following syntax.
children = ("Sally", "Hansel", "Gretel", "Svetlana")
(first_child, second_child, third_child, fourth_child) = children
print(first_child) # Output is "Sally"
print(second_child) # Output is "Hansel"
print(third_child) # Output is "Gretel"
print(fourth_child) # Output is "Svetlana"
Create a variable for the animals in your zoo tuple, and print them to the console.
Convert your tuple into a list.
Use extend() to add three more animals to your zoo.
Convert the list back into a tuple.
'''

# zoo tuple
zoo = ("cheetah", "python", "penguin", "black bear", "grizzly bear", "lion", "ibex", "water buffalo", "hyena", "bald eagle")

# find animal using tuple.index(value)
print(zoo.index('penguin'))
print(zoo.index('python'))

# find animal using tuple syntax
animal_to_find = "black bear"
if animal_to_find in zoo:
    print(f'{animal_to_find} was found')

# ignore many values using the *_ syntax in the assignment:
(first_animal, second_animal, third_animal, *_) = zoo
print(first_animal, second_animal)

zoo_list = list(zoo)
zoo_list.append('tiger')
zoo_list.append('parrot')
zoo_list.append('falcon')
print(zoo_list)

print(tuple(zoo_list))