def add(x,y):
    """adding the two parameters"""
    return x + y

def substract(x,y):
    """substracting the two parameters"""
    return x - y

def multiply(x,y):
    """multiplying the two parameters"""
    return x * y

def divide(x,y):
    """dividing the two parameters"""
    return x/y if y!=0 else "Error! Division by Zero"


def modulus(x,y):
    """modulus between the two parameters"""
    return x%y

def power(x,y):
    """x power y"""
    return x**y

to_operate = {"+":add,"-":substract,"*":multiply,"/":divide,"%":modulus,"**":power}


print("Welcome to Simple Calculator")

while True:
    num1 = float(input("Enter the first number : "))
    operator = input("Enter Operator (+,-,*,/,**,%) : ")
    num2 = float(input("Enter the second number : "))


    if operator in to_operate:
        print("Operation : ",to_operate[operator])
        result = to_operate[operator](num1,num2)

        print("Result" , result)

    else:
        print("Invalid Operator!")

        if operator in to_operate:
            result = to_operate[operator](num1,num2)
            print("Result : ", result)
        
        else:
            print("Invalid operator!")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")

        
    if another_calculation.lower() != 'yes':
        break