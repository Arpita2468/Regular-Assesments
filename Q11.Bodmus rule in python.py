def evaluate_expression(expression):
    try:
        result = eval(expression) 
        return result
    except Exception as e:
        print("Error evaluating expression:", e)
        return None
expression = input("Enter a mathematical expression: ")
result = evaluate_expression(expression)
if result is not None:
    print("Result of '" + expression + "':", result)
