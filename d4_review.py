#import time

#file = time.strftime("%Y%m%d-%H%M%S")
#print 'Code to save data to a file named:', file

def changeabletype():
    a = 10
    print 'First, variable a has value', a, 'and type', type(a)
    a = 3.14159
    print 'Now, variable a has value', a, 'and type', type(a)
    a = 'ABC'
    print 'Now, variable a has value', a, 'and type', type(a)

def tupleassign():
    x, y, z = 'hola', -45, 0.5
    print 'x=',x,' y=',y,' z=',z

def printsControl():
    print('A\nB\nC')
    print('D\tE\tF')
    print('WX\bYZ')
    print('1\a2\a3\a4\a5\a6')

def scientificnotation():
    avogadros_number = 6.022e23
    c = 2.998e8
    print "Avogadro's number = ", avogadros_number
    print 'Speed of light = ', c

def escapequotes():
    print("Did you know that 'word' is a word?")
    print('Did you know that "word" is a word?')
    print('Did you know that \'word\' is a word?')
    print("Did you know that \"word\" is a word?")

def inputFunc():
    x = raw_input('Please enter some text: ')
    print 'Text entered:', x, 'Type:', type(x)
    x = int(raw_input('Please enter a Integer number: '))
    print 'Integer entered:', x, 'Type:', type(x)
    x = float(raw_input('Please enter a Float number: '))
    print 'Float entered:', x, 'Type:', type(x)

def tempConv():
    degreesF = int(raw_input('Enter the temperature in degrees F: '))
    degreesC = ((degreesF - 32) * (5.0/9.0)) #integer division is not posible, result = 0
    degreesK = 273 + degreesC
    print 'degrees F:', degreesF, 'degrees C:', degreesC, 'degrees K:', degreesK

def divisions():
    dividend = float(raw_input('Please enter a dividend number: '))
    divisor = float(raw_input('Please enter a divisor number: '))
    if divisor != 0 and dividend != divisor:
        print dividend, '/', divisor, "=", dividend/divisor
    elif dividend == divisor:
        print dividend, '/', divisor, "= Unidad"
    else:
        print 'Division by zero is not allowed'

def troubleshoot():
    print "Help! My computer doesn't work!"
    print "Does the computer make any sounds (fans, etc.)"
    choice = raw_input("or show any lights? (y/n):")
    if choice == 'n':
        choice = raw_input("Is it plugged in? (y/n):")
        if choice == 'n':
            print "Plug it in. If the problem persists, please run this program again"
        else:
            choice = raw_input("Is the switch in the \"on\" position? (y/n):")
            if choice == 'n': # The switch is off, turn it on!
                print "Turn it on.  If the problem persists, "
                print "please run this program again."
            else: # The switch is on
                choice = raw_input("Does the computer have a fuse? (y/n):")
                if choice == 'n': # No fuse
                    choice = raw_input("Is the outlet OK? (y/n):")
                    if choice == 'n': # Fix outlet
                        print "Check the outlet's circuit "
                        print "breaker or fuse.  Move to a"
                        print "new outlet, if necessary. "
                        print "If the problem persists, "
                        print "please run this program again."
                    else:
                        print "Please consult a service technician."
                else:
                    print "Check the fuse. Replace if "
                    print "necessary.  If the problem "
                    print "persists, then "
                    print "please run this program again."
    else:
        print "Please consult a service technician."

def forLoop():
    entry = 0   # Initialize entry
    sum = 0     # Initialize sum
    print "Enter numbers to sum 5 times, negative number ends list:"
    for n in range(0, 5):
        entry = int(raw_input("Number: "))
        if entry >= 0:
            sum += entry
        else:
            print "Negative number. Exit"
            break
        print (n + 1), "time, Sum =", sum   # n = 0 + 1 :. n = 1 the first time

def whileLoop():
    entry = 0   # Ensure the loop is entered
    sum = 0     # Initialize sum
    print "Enter numbers to sum, negative number ends list:"
    while entry >= 0:
        entry = int(raw_input("Number: "))
        if entry >= 0:
            sum += entry
        print "Sum =", sum

def whileBoolLoop():
    entry = 0   # Initialize entry
    sum = 0     # Initialize sum
    flag = True # Ensure the loop is entered
    print "Enter numbers to sum, negative number ends list:"
    while flag:
        entry = int(raw_input("Number: "))
        if entry >= 0:
            sum += entry
        else:
            print "Negative number. Exit"
            flag = False
        print "Sum =", sum


if __name__ == "__main__":
    forLoop()

