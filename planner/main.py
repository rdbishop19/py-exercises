from building import Building
from city import City

building_one = Building("205 N. 5th St.", 3)
building_one.purchase("Mike")
building_one.construct()

building_two = Building("820 N. 2nd St.", 7)
building_two.purchase("Karen")
building_two.construct()

building_three = Building("300 N. Lincoln", 12)
building_three.purchase("Mike")
building_three.construct()

building_four = Building("1143 W. Lawrence Ave.", 2)
building_four.purchase("Jim")
building_four.construct()

building_five = Building("12 Capital Ave.", 30)
building_five.purchase("Jim")
building_five.construct()

megalopolis = City("megalopolis","Invader Zim", "3012")

buildings = [building_one, building_two, building_three, building_four, building_five]

for building in buildings:
    megalopolis.add_building(building)
# Awesome code here

for building in megalopolis.buildings:
    building.print_report()