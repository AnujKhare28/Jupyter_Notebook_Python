class Calculator:

    @staticmethod
    def add(a,b):
        return a+b
    
    def sub(a,b):
        return a-b
    
    def mul(a,b):
        return a*b
    
    def div(a,b):
        if b == 0:
            raise ZeroDivisionError
        else:
            return a/b
        
x = int(input('Enter x: '))
y=int(input('Enter y: '))
print('')
print("Addition:", Calculator.add(x,y))
print('Subtraction:',Calculator.sub(x,y))
print('Multiplication:', Calculator.mul(x,y))

try:
    res = Calculator.div(x,y)
    print('Division:',res)
except:
    print('Division by zero error!')