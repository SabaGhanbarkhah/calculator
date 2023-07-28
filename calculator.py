#calculating two operands
#functions
def add(number1,number2):
    print ("{} + {} =".format(number1,number2),number1+number2)


def subtraction(number1,number2):
    print ("{} - {} =".format(number1,number2),number1-number2)

def multiplication(number1,number2):
    print ("{} * {} =".format(number1,number2),number1*number2)


def division(number1,number2):
    print ("{} / {} =".format(number1,number2),number1/number2)


#start
number1=int(input("Enter your first number: "))
a=input("Enter your operator: ")
number2=int(input("Enter your second number: "))

if a == "+":
    add(number1,number2)
elif a == '-' :
    print(subtraction(number1,number2))
elif a == "*" :
    print(multiplication(number1,number2))
elif a == "/" :
    print(division(number1,number2))
else:
    print("Error! invalid operator")

