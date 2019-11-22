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
def sub_two_no(a,b):
    diff = a - b
    return diff
z = sub_two_no(45,12)
print(z)

def hello_name(name):
    greetings = 'Hello {}!'.format(name)#dot format used in str
    return greetings
c = hello_name("Gerald")
print(c)
