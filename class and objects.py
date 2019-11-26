class Person:
    #class attribute means every object of the class by default will be a homo sapien
    species = "Homo Sapien"
    #Methods- a function that are defined  inside a class
    #init method / constructor - it runs as soon as you create an object
    def __init__(self, name, age):
        print("I am the constructor method")
        self.jina  = name
        self.miaka = age
    #self refer to name you will add
    def walk(self):
        print("{} is walking".format(self.jina))
pl2 =Person("Mbugua",22)
print(pl2.jina)
print(pl2.miaka)
pl2.walk()


#INSTANCE ATTRIBUTES/ATTRIBUTES - data unique only for that instance
#p1 = Person()
#print(p1.species)
# p2 = Person()
# p2.name = "Phares"
# p2.age = 45
# p2.walk()
# #print(type(p2))
# p3 = Person()
# p3.name = "Mbugua"
# print(p3.name)
# p3.age = 34
# p3.marital_status = ("True","False")
# p3.citizenship = "Kenyan"
# p3.Gender = ("Male","Female")
# p3.walk()
# print(p3.walk)
# print(p3.age)
# print(p3.marital_status)

# class Car:
#     make ="Subaru"
#     wheels = 4
#     YOM = 2012
#     def park(self):
#         print("{} is been parked under Block B".format(self.make))
#
#
# C1 = Car()
# print(C1.make)
# C1.park()
# print(C1.park)
# C1.wheels

class Student:
    school_name = "abc Primary School"
    #class 5
    #name = m,e,scs,sst,k
    #create method
    #1.fing total marks(total_marks())
    #2.find average score (average_score())
    #3.fing grade (grade_student())