import re

class Calculator:
    def __init__(self):
        self.current_value = 0

    @staticmethod
    def peek(stack):
        return stack[-1] if stack else None

    @staticmethod
    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        formula = f"{left}{operator}{right}"
        values.append(eval(formula))

    @staticmethod
    def greater_precedence(op1, op2):
        precedences = {'+': 0, '-': 0, '*': 1, '/': 1}
        return precedences[op1] > precedences[op2]

    def calculate(self):
        user = ""
        while user != "END":
            user = input("Type in an expression (or END to quit): ")
            if user == "END":
                break

            
            tokens = re.findall(r"\d+\.\d+|\d+|[a-zA-Z_]\w*|[+*/()-]", user)

            values, operators = [], []

            for token in tokens:
                
                try:
                    if '.' in token:
                        values.append(float(token))
                    else:
                        values.append(int(token))
                except ValueError:
                    
                    if token == '(':
                        operators.append(token)
                    elif token == ')':
                        while self.peek(operators) != '(':
                            self.apply_operator(operators, values)
                        operators.pop()
                    else:
                        while self.peek(operators) and self.peek(operators) not in "()":
                            if self.greater_precedence(self.peek(operators), token):
                                self.apply_operator(operators, values)
                            else:
                                break
                        operators.append(token)

            
            while self.peek(operators):
                self.apply_operator(operators, values)

            
            self.current_value = values[0]
            print("Result:", self.current_value)



calc = Calculator()
calc.calculate()




    




        


