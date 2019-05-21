# Python Program to find Factors of a Number

number = int(input("Please Enter any Number: "))

value = 1
print("Factors of a Given Number {0} are:".format(number))

while (value <= number):
    if (number % value == 0):
        if (value % 2 == 0):
            print(str("{0}".format(value)+" is an even factor"))
        else:
            print(str("{0}".format(value) + " is an odd factor"))
    value = value + 1
