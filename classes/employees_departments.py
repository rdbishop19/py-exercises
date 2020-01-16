'''
Create an Employee type that contains information about employees of a company.
 Each employee must have a name, job title, and employment start date.
Create a Company type that employees can work for.
A company should have a business name, address, and industry type.

Create two companies, and 5 people who want to work for them.
Assign 2 people to be employees of the first company.
Assign 3 people to be employees of the second company.
Output a report to the terminal the displays a business name, and its employees.
For example:

Acme Explosives is in the chemical industry and has the following employees
   * Michael Chang
   * Martina Navritilova

Jetways is in the transportation industry and has the following employees
   * Serena Williams
   * Roger Federer
   * Pete Sampras
'''
class Employee:
    def __init__(self, first_name, last_name, job_title, start_date):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.start_date = start_date

class Company:
    def __init__(self, business_name, address, industry_type):
        self.business_name = business_name
        self.address = address
        self.industry_type = industry_type
        self.employees = list()

    def add_employee(self, employee):
        self.employees.append(employee)

apple = Company("Apple", "101 Jobs Ave", "Electronics")
lenovo = Company("Lenovo", "1 Thinkpad Dr.", "Computers")

ryan = Employee("Ryan", "Bishop", "Technician", "2019-09-30")
trey = Employee("Trey", "Suiter", "Lead Excruciator", "2020-01-16")
julian = Employee("Julian", "Garcia", "Meme Technician", "2020-01-01")
sam = Employee("Sam", "Pita", "Developer", "2020-03-27")
joe = Employee("Joe", "Shepherd", "Game Developer", "2006-01-20")

apple.add_employee(julian)
apple.add_employee(joe)
lenovo.add_employee(ryan)
lenovo.add_employee(sam)
lenovo.add_employee(trey)

def print_employees(company):
    print(f'{company.business_name} is in the {company.industry_type} industry and has the following employees:')
    for employee in company.employees:
        print(f'* {employee.first_name} {employee.last_name}')
    print()

print_employees(apple)
print_employees(lenovo)
