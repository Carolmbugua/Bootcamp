"""
create a program to ask for marks for 5 subjects ie MATH,ENG,KISWA,SCS,SST
Find the total marks
the average
grade the student
rank

Eng_Marks =int (input("Enter eng number:"))
if kisw < 0 or kisw >100:
Kisw_Marks = int(input("Enter kisw number:"))
SST_Marks = int(input("Enter sst number:"))
Math_Marks = int(input("Enter math number:"))
Scs_Marks = int(input("Enter scs number:"))
Total_Marks = (Eng_Marks + Kisw_Marks + SST_Marks + Math_Marks +Scs_Marks)
print(Total_Marks)
Average_Marks = (Total_Marks/5)
print(Average_Marks)
#A > 79 , B - 60 to 78, C - 59 to 49, D - 48 to 40, E - less 40

Average_Marks =90
if 90>Average_Marks>79:
    print("Grade A")
elif(78>Average_Marks>60):
    print("Grade B")
elif(59>Average_Marks>49):
    printt("Grade c")
elif(59>Av)

taskList = [23, "Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John")]
print(type(taskList))
print(taskList[2][2])
print(taskList[2][1])
print(len(taskList))
print(str(taskList[-2])[::-1])
print(taskList[4][1].replace("John","Jane"))
print(taskList[2][2] ['currency'].replace("KES","$"))
#write a loop tha calculates the same results as 5**3 using muiltiplicatiom( and with out exponentiation)
result = 1
for number in range(0,4):
 result=result*5
print(result)
string="Newton"
r =string[::-1]
print(r)
newstring =""
oldstring = "Newton"
for char in oldstring:
    newstring = char + newstring
print(newstring)

names = ["Carolyne","Mbugua"]
for char in enumerate(names):

    print(char )"""


x = list(range(0,21))
evenNumber = []
oddNumber = []
for i in x: #i - variable to be asigned,x - list,tuple,dict
    print(i)
    if i %2 ==0:
        evenNumber.append(i)
    else:
        oddNumber.append(i)
print(evenNumber)
print(oddNumber)






"""odd =
sim_password =int(input("Enter my password:"))
print(sim_password)"""