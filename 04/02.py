from stack import Stack

def is_balanced(expression):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in brackets.keys():
            # If the character is an opening bracket, push it onto the stack.
            stack.append(char)
        elif char in brackets.values():
            # If the character is a closing bracket, check if it matches the top of the stack.
            if not stack or brackets[stack.pop()] != char:
                return False
        else:
            # Ignore characters other than brackets.
            continue

    # If the stack is empty, all brackets are balanced.
    return not stack

# Driver Code
if __name__ == "__main__":
    expression = input("Enter an expression: ")
    if is_balanced(expression):
        print(f"The expression '{expression}' has balanced parentheses.\n")
    else:
        print(f"The expression '{expression}' does not have balanced parentheses.\n")
