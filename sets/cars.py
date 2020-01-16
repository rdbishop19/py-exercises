'''
Create an empty set named showroom.
Add four of your favorite car model names to the set.
Print the length of your set.
Pick one of the items in your show room and add it to the set again.
Print your showroom. Notice how there's still only one instance of that model in there.
Using update(), add two more car models to your showroom with another set.
You've sold one of your cars. Remove it from the set with the discard() method.

'''

# initialize empty set
showroom = set()
showroom.add("Porsche 911 Turbo GT")
showroom.add("Ford Mustang Shelby GT")
showroom.add("Audi R8")
showroom.add("Maserati GranTurismo")
showroom.add("Maserati GranTurismo")
showroom.update(["Tesla Model S", "Mini Cooper"])
showroom.discard("Mini Cooper")

print(showroom)
print(len(showroom))

'''
Acquiring more cars
Now create another set of cars in a variable junkyard. 
Someone who owns a junkyard full of old cars has approached you 
about buying the entire inventory. 
In the new set, add some different cars, but also add a few that are 
the same as in the showroom set.
Use the intersection method to see which cars exist in both the showroom and that junkyard.
Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.
'''

junkyard = set()
junkyard.add("Porsche 911 Turbo GT")
junkyard.add("Buick Century")
junkyard.add("Tesla Model S")
print(junkyard)
# print(junkyard.intersection(showroom))
new_showroom = showroom.union(junkyard)
print(new_showroom)
new_showroom.discard("Buick Century")
print(new_showroom)