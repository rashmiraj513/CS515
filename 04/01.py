from stack import Stack

# Function to evaluate the postfix operations
def evaluate_postfix(expression):
    stack = Stack()
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y}

    # Postfix Expression evaluation
    for token in expression.split(" "):
        if token.isdigit():
            # If the token is a digit, push it onto the stack.
            stack.push(int(token))
        elif token in operators:
            # If the token is an operator, pop two operands from the stack,
            # apply the operator, and push the result back onto the stack.
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[token](operand1, operand2)
            stack.push(result)
        else:
            # If the token is neither a digit nor an operator, raise an error.
            raise ValueError("Invalid token in expression: {}".format(token))

    # After processing all tokens, the result should be the only item left on the stack.
    return stack.pop()


# Driver Code
if __name__ == "__main__":
    postfix_expression = input("Enter an expression (Please enter components with one space): ")
    result = evaluate_postfix(postfix_expression)
    print("Result of expression '{}': {}".format(postfix_expression, result))