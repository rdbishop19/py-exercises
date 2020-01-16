'''
Properties
designer - It will hold your name.
date_constructed - This will hold the exact time the building was created.
owner - This will store the same of the person who owns the building.
address
stories
Methods
Define a construct() method. The method's logic should set the date_constructed field's value to datetime.datetime.now(). You will need to have import datetime at the top of your file.

Define a purchase() method. The method should accept a single string argument of the name of the person purchasing a building. The method should take that string and assign it to the owner property.
'''
import datetime

class Building:
    def __init__(self, address, stories):
        self.address = address
        self.stories = stories
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
    
    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, buyer):
        self.owner = buyer

'''
Create 5 building instances
Have each one get purchased by a real estate magnate
After purchased, construct each one
Once all building are purchased and constructed, 
print the address, owner, stories, and 
date constructed to the terminal for each one.
800 8th Street was purchased by Bob Builder on 03/14/2018 and has 12 stories.
'''
def print_report(building):
    print(f'{building.address} was purchased by {building.owner} on {building.date_constructed} and has {building.stories} stories.')

building_one = Building("205 N. 5th St.", 3)
building_one.purchase("Mike")
building_one.construct()
print_report(building_one)

building_two = Building("820 N. 2nd St.", 7)
building_two.purchase("Karen")
building_two.construct()
print_report(building_two)

building_three = Building("300 N. Lincoln", 12)
building_three.purchase("Mike")
building_three.construct()
print_report(building_three)

building_four = Building("1143 W. Lawrence Ave.", 2)
building_four.purchase("Jim")
building_four.construct()
print_report(building_four)

building_five = Building("12 Capital Ave.", 30)
building_five.purchase("Jim")
building_five.construct()
print_report(building_five)

# print(building_one.date_constructed)