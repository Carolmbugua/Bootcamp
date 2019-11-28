#class Person:

    #class attribute means every object of the class by default will be a homo sapien
# Methods- a function that are defined  inside a class,action that can be performed on an object
# init method / constructor - it runs as soon as you create an object
#     species = "Homo Sapien"
#     def __init__(self, name, age):
#         print("I am the constructor method")
#         self.jina = name
#         self.miaka = age
#          # self refer to name you will add
#
#     def walk(self):
#          print("{} is walking".format(self.jina))
#
#
# pl2 = Person("Mbugua",23)
# print(pl2.jina)
# print(pl2.miaka)
# pl2.walk()


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
#for principle of oop - inheritance
# C1 = Car()
# print(C1.make)
# C1.park()
# print(C1.park)
# C1.wheels

class Student:
    school_name = "ABC Primary School"
    station = 5
    def __init__(self,station,math,kisw,eng,scs,sst):
        self.M = math
        self.E = eng
        self.K = kisw
        self.S = scs
        self.SS = sst
        self.ST = station

    def total_marks(self):
         return self.M + self.E + self.K + self.S + self.SS

    def average_score(self):
        return (self.M + self.E + self.K + self.S + self.SS) / 5

    def grade_student(self):
       average =self.average_score()


       if 100>= average>=80:
           return("GRADE A")
       elif 79>average>70:
           return("GRADE B")
       elif 69 >=average>=60:
           return "GRADE C"
       elif 59 >=average>=50:
           return "GRADE D"
       else:
           return "invalid marks"



sch = Student("class 5 :",45,67,45,34,67,)
print(sch.school_name)
print(sch.total_marks())# sch.average_score()
print(sch.grade_student())
print(sch.average_score())
# total_marks()

    #name = m,e,scs,sst,k
    #create method
    #1.fing total marks(total_marks())
    #2.find average score (average_score())
    #3.fing grade (grade_student())








