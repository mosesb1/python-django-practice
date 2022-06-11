# class Sample():
#     species = 'Human'
#     planet = 'Earth'

#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
    


# stu1 = Sample('moses',4.0)
# stu2 = Sample('mimi', 3.5)
# print(stu1.name, stu1.gpa)
# print(stu2.species, stu2.gpa)

class Agent():
    origin = 'United States'

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
    
    def area(self):
        return pow(self.radius,2)*Circle.pi
    
    def circumference(self):
        return 2*self.radius*Circle.pi

    def multiply_radius(self, num):
        self.radius = self.radius * num

class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        print('hello')
    
    def report(self):
        print(f"I am {self.first_name} {self.last_name}")

class Agent(Person):

    def __init__(self, first_name, last_name, code_name):
        Person.__init__(self, first_name, last_name)
        self.code_name = code_name

    def report(self):
        print('I am here')

    def reveal(self,passcode):
        if passcode == 123:
            print('I am a secret agent')
        else:
            self.report()

x = Agent("John","Smith","Viper")
x.hello()
x.reveal(121)
print(x.code_name)