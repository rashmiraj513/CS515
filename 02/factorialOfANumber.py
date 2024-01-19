# Function to calculate factorial of a number
def calculateFactorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

val = int(input("Enter a number: "))
print("The factorial of {} is {}.".format(val, calculateFactorial(val)))