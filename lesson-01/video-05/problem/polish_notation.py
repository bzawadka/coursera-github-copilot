def polish_notation(expression):
    expression = expression.split()
    operators = ['+', '-', '*', '/']
    stack = []
    for i in range(len(expression)):
        if expression[i] in operators:
            operator = expression[i]
            operand1 = stack.pop()
            operand2 = stack.pop()
            if operator == '+':
                result = operand1 + operand2
            elif operator == '-':
                result = operand2 - operand1
            elif operator == '*':
                result = operand1 * operand2
            elif operator == '/':
                result = operand2 / operand1
            stack.append(result)
        else:
            stack.append(int(expression[i]))
    return stack[0]


def reverse_polish_notation(expression):
    expression = expression.split()
    operators = ['+', '-', '*', '/']
    stack = []
    for i in range(len(expression) - 1, -1, -1):
        if expression[i] in operators:
            operator = expression[i]
            operand1 = stack.pop()
            operand2 = stack.pop()
            if operator == '+':
                result = operand1 + operand2
            elif operator == '-':
                result = operand1 - operand2
            elif operator == '*':
                result = operand1 * operand2
            elif operator == '/':
                result = operand1 / operand2
            stack.append(result)
        else:
            stack.append(int(expression[i]))
    return stack[0]