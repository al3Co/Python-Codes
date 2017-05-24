# function (value, value)
#   operatios = value operations
#   return operations

def simpleFunction():
    print 'Add code here'

def greeting(name, message = 'Hello'):
    print message, name

def calculate(amount, discount):
    return amount - (amount * discount / 100)

if __name__ == "__main__":
    simpleFunction()
    
    greeting('Pepe Grillo')             # Prints: Hello Pepe Grillo
    
    calculation = calculate(100, 30)    # Returns data
    print calculation
