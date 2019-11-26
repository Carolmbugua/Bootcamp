#def keyword
def print_hello_word():
        print("hello world")
#         print("am fine")
#     #body of the function
# print_hello_word()
# print_hello_word()
# print_hello_word()
# print_hello_word()
# print_hello_word()
# print_hello_word()
# print_hello_word()
# print_hello_word()
x = list(range(0,9))
print(x[0])
y = list(range(7,60))
print(y[0])
t = list(range(100,200,5))
print(t[0])
def get_first_list_item(alist):
    print(alist[0])
get_first_list_item(x)
get_first_list_item(y)
get_first_list_item(t)

# parameter a variable to store
# x = "carol"
# def my_name() :
#     print(x)
# my_name()
# def print_my_name(aname):
#     print(aname)
# print_my_name("carol")
# def add_two_numbers(a,b):
#     result = a + b
#     print(result)
# add_two_numbers(12,34)
# add_two_numbers(122,354)
# add_two_numbers(172,734)
"""def sub_two_no(a,b):
    diff = a - b
    return diff
z = sub_two_no(45,12)
print(z)

def hello_name(name):
    greetings = 'Hello {}!'.format(name)#dot format used in str
    return greetings
c = hello_name("Gerald")
print(c)
#FUNCTION PRACTICAL 1
def finding_grades(Eng,Kisw,Math,Scs,Stt):
    total_marks = Eng + Kisw + Math + Scs + Stt
    return total_marks
t = finding_grades(56,76,89,89,90)
print(t)
average_marks = t / 5
print(average_marks)
if 90 >average_marks >70:
    print("grade A")
elif 69 >average_marks >50:
    print("grade B")
elif 49 > average_marks> 40:
    print(Fail)
else:
    print()

#practice 2

def sum_digits(num):
    return 0 if num == 0 else int(num%10) + sum_digits(int(num/10))

tnum = sum_digits(67586)
print(tnum)
#OR
def sum_digits(num):
    sum = 0
    while (num > 0):
        sum += int(num%10)
        num = int(num/10)
    return sum
tnum = sum_digits(68532578)
print(tnum)

#TASK 1
word = []
text = input("Enter a word:")
if text == "yes":
    print("Yes")
elif text == "Yes":
    print("Yes")
elif text == "YES":

    print("Yes")

else:
    print("NO")

def max_value(var1,var2,var3):
    max_3 = 0
    if(var1>var2) and (var1>var3):
        print("var1 is the largest!")
    elif(var2>var1) and (var2>var3):
        print("var2 is the largest!")

    else:
        print("var 3 is the largest")
max_value(45,67,9)

def max_of_three(a,b,c):
    rext =[a,b,c]
    print(sorted(rext)[-1])
    return rext[-1]
t = max_of_three(2,3,5)
print(t)

a = [5, 10, 15, 20, 25]
def first_lastvalue(a):
    return(a[0],a[-1])
b = first_lastvalue(a)
print(b)

def new_list(alist):

    return(alist[0],alist[-1])


    k = [2,4,5,6,8]
    j = []
    for i in k:
       j.append(i)
print(new_list(j))
#example
a_list = range(1,21)
def printValues(a_list):
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l[:5],l[-5:])


printValues(a_list)"""

numbers = (1,2,3,4,5,6,7,8,9,10)
print(numbers[:4])
print(numbers[-5:])
#or
numbers = (1,2,3,4,5,6,7,8,9,10)
first_half =[]
scond_half = []
for i in range(0,5):
    first_half.append(numbers[i])
for i in range(5,10):
    scond_half.append(numbers[i])
print(first_half)
print(scond_half)









#values=input("enter the values with commas").split(",")

#c=[values[0],values[-1]]




