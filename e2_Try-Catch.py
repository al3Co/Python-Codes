# While True
# try catch
# break


def tryCatchGeneric():
    while True: # Undetermined cycle
        try:    # Try to do the following code
            x = input("Please enter a number: ")
            print x, type(x)
            break   # Beaks any cycle
        except Exception, e:    # Takes any error and saves it in "e"
            print ('Error: ', e)

def tryCatchInt():
    while True:
        try:
            x = int(raw_input("Please enter a Integer: "))
            print x, type(x)
            break
        except Exception, e:
            print ('Error: ', e)

def tryCatchFloat():
    while True:
        try:
            x = float(raw_input("Please enter a float: "))
            print x, type(x)
            break
        except Exception, e:
            print ('Error: ', e)

def tryCatchString():
    while True:
        try:
            x = raw_input("Please enter a string: ")
            print x, type(x)
            break
        except Exception, e:
            print ('Error: ', e)

def example():
    while True:
        try:
            x = int(raw_input("Please enter a Integer 1: "))
            y = int(raw_input("Please enter a Integer 2: "))
            print 'Sum = '+ str(x + y)
            break
        except (ValueError), e:
            print 'Invalid number try again, error:', e

if __name__ == "__main__":
    example()

