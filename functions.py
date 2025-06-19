#1. Built-Functions/Standard Library Function

x = max(67, 80, 90, 20, 10)
print("The maximum number is :", x)

y = min(67, 80, 90, 20, 10)
print("The minimum number is :", y)

z = pow(2, 3)
print("The power of 2 to 3 is :", z)


#2. User-Defined Functions
def greeting():
    print("Hello World!")

greeting()  #Calling a function

def school():
    print("My coding school is eMobilis")

school()

#parameters and Arguments
def add(num1, num2):
    print(num1 + num2)

add(5, 10)
add(20, 10)


def student(fullname, course, gender):
    print(fullname, course, gender)

student("Mary Mbotela", "MIT", "female")
student("James Otieno", "MIT", "male")
student("Mildred Kamau", "MIT", "female")


# A python program that displays details of five employees
# Fintech using parameter and argument(Fullname, email, age, position, salary, marriage status)

def employee(fullname, email, age, position, salary, marriage_status):
    print(fullname, email, age, position, salary, marriage_status)

employee("John Mali", "john1@gmail.com", 37, "Senior manager", 50000, "married")
employee("Jane Atieno", "jane2@gmail.com", 28, "Assistant manager", 32000, "single")
employee("Bob Smith", "bob3@gmail.com", 30, "Marketing Officer", 43000, "married")
employee("Sheila Khan", "sheila4@gmail.com", 25, "Secretary", 30000, "single")
employee("Mark Baraka", "mark5@gmail.com", 32, "Supervisor", 40000, "married")
employee("Peter Mwangi", "peter6@gmail.com", 35, "Director", 45000, "married")











