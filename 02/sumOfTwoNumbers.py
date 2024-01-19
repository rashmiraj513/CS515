# Approach 1: Using plus (+) operator when values are hard-coded.
first_number = 12
second_number = 32
sum = first_number + second_number
print("The sum of {} and {} is {}.".format(first_number, second_number, sum))

# Approach 2: Using plus (+) operator after taking the input from the user
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
sum = first_number + second_number
print("The sum of {} and {} is {}.".format(first_number, second_number, sum))

# Approach 3: Using user-defined function when argument is passed
def sumWithArgs(a, b):
    return a + b
print("The sum of {} and {} is {}.".format(12, 23, sumWithArgs(12, 23)))

# Approach 4: Using user-defined function after taking the user input
def sumWithUserInput():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("The sum of {} and {} is {}.".format(a, b, a + b))
sumWithUserInput()

# Approach 5: Using Lambda Functions
sumUsingLambda = lambda x, y : x + y
print("The sum of {} and {} is {}.".format(5, 12, sumUsingLambda(5, 12)))


# Approach 6: Without using any extra variables
print("The sum of is {}.".format((float(input("Enter first number: ")) + float(input("Enter second number: ")))))

# Approach 7: Without using plus (+) operator
def sumWithoutPlusOperator(a, b):
    if(a != b):
        # Using a^2 - b^2 = (a + b)(a - b) formula
        return (a * a - b * b) / (a - b)
    return 2 * a
print("The sum of {} and {} is {}.".format(5, 12, sumWithoutPlusOperator(5, 12)))