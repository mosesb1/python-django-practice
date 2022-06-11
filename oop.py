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

mycircle = Circle(radius = 20)
mycircle.multiply_radius(2)
print(mycircle.area(), mycircle.circumference())