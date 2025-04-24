def add(x,y): #this is for adding
    return x+y
def sub(x,y): #subtracting
    return x-y
def div(x,y): #dividing
    if y==0:
        return "You cannot divide by zero, please enter a valid number!"    
    else:
        return x/y
def mul(x,y): #multiplying
    return x*y
def pow(x,y): #x to the power of y, like x^y
    return x**y
def calculator():
    print("Welcome to the Simple Calculator. Please choose from our five options of calculations that only receive TWO numbers at a time. Your options are adding, subtracting, dividing, multiplying, and raising the first number by the second's power. Please input a number in the next block of text to pick from (1)addition, (2)subtraction, (3)division, (4)multiplication, (5)raising power.")

while True:
    a = input("Please pick from 1-5. ")
    if a in ["1","2","3","4","5"]:
        try:
            num1 = input("Excellent. Please enter your first number. ")
            num2 = input("Now please enter your second number. ")
        except ValueError:
            print("Please input a value in between 1-5 to pick from (1)addition, (2)subtraction, (3)division, (4)multiplication, (5)raising power.")
            continue
        if a == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif a == '2':
            print(f"{num1} - {num2} = {sub(num1, num2)}")

        elif a == '3':
            print(f"{num1} * {num2} = {mul(num1, num2)}")

        elif a == '4':
            print(f"{num1} / {num2} = {div(num1, num2)}")

        elif a == '5':
            print(f"{num1} ^ {num2} = {pow(num1, num2)}")

            next_calculation = input("Let's do another calculation? (y/n): ")
            if next_calculation.lower() != 'y':
                break
        else:
            print("Invalid Input!")

        if __name__ == "__main__":
            calculator()