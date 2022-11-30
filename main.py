import math
import sys

class Calculator:
    ''' The class includes the single class method which performs basic mathematical operations on the numbers got from the client inputs in the console.'''
    @classmethod
    def calculate(cls):
        print('\nWelcome to the Calculator app!\n\n'
        'The Calculator performs basic mathematical operations.\n' 
        'In order to get a result, please, enter one of the mathematical operators (+, -, *, / or **)\n' 
        'and a number, separated by a space.\n'
        'The result is kept in memory and you can proceed with next calculations on the basis of this intermediary result.\n'
        'You can also take a quadratic root from the number in the result by entering <sqrt>.\n'
        'In order to reset the result, enter <reset>.\n'
        'If you want to stop the calculation, get the final result and exit, enter <quit>.')
        result = 0
        i = 0
        while True: # the calculations are looped until a client enters 'quit'
            cls.input = input().split()
            try:
                if cls.input[0] == "+": # the addition is performed if the client enters '+' and a number
                    if len(cls.input) > 2 or len(cls.input) == 0: # the client should not enter more than two symbols.  :
                        print(f'Please, enter a mathematical operator and a number,\n'
                        'separated by a space.')
                    else:
                        result = result + float(cls.input[1])
                        print(f'Result: {result}')
                elif cls.input[0] == "-": # the subtraction is performed if a client enters '-' and a number
                    if len(cls.input) > 2 or len(cls.input) == 0: # the client should not enter more than two symbols.
                        print(f'Please, enter a mathematical operator and a number,\n'
                        'separated by a space.')
                    else:
                        result = result - float(cls.input[1])
                        print(f'Result: {result}')
                elif cls.input[0] == "*": # the  multiplication is performed if a client enters '*' and a number
                    if len(cls.input) > 2 or len(cls.input) == 0: # the client should not enter more than two symbols.
                        print(f'Please, enter a mathematical operator and a number,\n'
                        'separated by a space.')
                    else:
                        try:
                           result = result * float(cls.input[1])
                           print(f'Result: {result}')
                        except: # the result should not exceed the maxmimum number which could be processed by the operational system
                            result > sys.maxsize
                            print("The number is too large.")
                elif cls.input[0] == "**": # the result is raised by the degree if a client enter '**' and a number
                     if len(cls.input) > 2 or len(cls.input) == 0: # the client should not enter more than two symbols.
                         print(f'Please, enter a mathematical operator and a number,\n'
                         'separated by a space.')
                     else:
                         try:
                            result = result ** float(cls.input[1])
                            print(f'Result: {result}')
                         except: # the result should not exceed the maxmimum number which could be processed by the operational system
                            result > sys.maxsize
                            print("The number is too large.")
                elif cls.input[0] == "/": # the division is performed if a client enters '/' and a number
                     if len(cls.input) > 2 or len(cls.input) == 0: # the client should not enter more than two symbols.
                         print(f'Please, enter a mathematical operator and a number,\n'
                         'separated by a space.')
                     else:
                         try:
                            result = result / float(cls.input[1])
                            print(f'Result: {result}')
                         except ZeroDivisionError: # the division by zero is not allowed, a client receives the following message.
                            print('Division by zero is not a legal mathematical operation.')
                elif cls.input[0] == "sqrt": # if a client enters 'sqrt' a square root is taken from the number kept in the memory as a result o a previous operation
                    if len(cls.input) > 1 or len(cls.input) == 0: # the client should not enter more than one string.
                        print(f'Please, just enter <sqrt>.')
                    else:
                        result = math.sqrt(result)
                        print(f'Result: {result}')
                elif cls.input[0] == "reset": # if client enters 'reset', the result in the memory is nullified
                        if len(cls.input) > 1  or len(cls.input) == 0: # the client should not enter more than one string.
                            print(f'Please, just enter <reset>.')
                        else:
                            result = 0
                            print(f'Result: {result}')
                elif cls.input[0] == "quit": # a client has an option to exit from the app by entering 'quit'
                    if len(cls.input) > 1 or len(cls.input) == 0:   # the client should not enter more than one string.
                        print(f'Please, just enter <quit>.')
                    else:
                        result = result
                        print(f'You have stopped the calculation.\n' 
                        f'The final result is {result}.')
                        break
                else: # if the input does not satisfy the requirements presented in the description, a client receives the following message and get the opportunity to correct his or her input
                    print(f'Please, enter a mathematical operator and a number,\n'
                    'separated by a space.')
                i += 1
            except ValueError:
                assert ValueError(print("Please, enter a mathematical operator and a number,\n"
                        "separated by a space."))
                i += 1
            except IndexError:
                assert IndexError(print("Please, enter a mathematical operator and a number,\n"
                                 "separated by a space."))
                i += 1

if __name__ == '__main__':
    Calculator.calculate()
