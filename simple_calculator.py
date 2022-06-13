while True:
    try:
        first = float(input("Enter your first number: "))
    except ValueError:
        print("Pls enter an integer or decimal number")
        continue
    else:
        break


while True:
    try:
        second = float(input("Enter your second number: "))
    except ValueError:
        print("Pls enter an integer or decimal number")
        continue
    else:
        break


print("1. addition")
print("2. subtraction")
print("3. division")
print("4. multiplication")
print("5. modulus")

index = (1,2,3,4,5)
options = ("addition", "subtraction", "division", "multiplication", "modulus")
response = ("sum of", "difference between", "ratio of", "product of", "modulus of")


while True:
    try:
        operator = int(input("Pls select a math operation to perform: "))
        if operator not in index:
            print("Enter a number from 1 to 5")
            continue
    except ValueError:
        print("Enter a number from 1 to 5")
        continue
    else:
        break


try:
    add = first + second
    diff = first - second
    div = first / second
    prod = first * second
    mod = first % second
    answer = [add, diff, div, prod, mod]
    print(f"The {response[operator-1]} {first} and {second} is {answer[operator-1]}")
except ZeroDivisionError:
    print("Sorry, you can not divide a number by zero")