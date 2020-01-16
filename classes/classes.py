'''
Create a Pizza type for representing pizzas in Python. 
 about some basic properties that would define a pizza's values; 
 things like size, crust type, and toppings would help. 
 Define those in the __init__ method so each instance can have 
 its own specific values for those properties.

Add a method for interacting with a pizza's toppings, 
called add_topping.

Add a method for outputting a description of the pizza 
(sample output below).

Make two different instances of a pizza. 
If you have properly defined the class, you should be able to 
do something like the following code with your Pizza type.
'''

class Pizza:
    def __init__(self):
        # initialize the pizza object
        self.size = "medium"
        self.crust_type = "hand-tossed"
        self.toppings = ["cheese"]

    def add_topping(self, topping):
        self.toppings.append(topping)

    def print_order(self):
        print(f'I would like a {self.size} {self.crust_type} with {" and ".join(self.toppings)}')

pizza_one = Pizza()
pizza_one.size = "large"
pizza_one.crust_type = "deep dish"
pizza_one.add_topping("pepperoni")
pizza_one.add_topping("sausage")
pizza_one.add_topping("onions")

pizza_two = Pizza()

pizza_one.print_order()
pizza_two.print_order()

