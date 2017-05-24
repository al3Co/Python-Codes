# For cycle

def forInRange():
    for x in range(5):          # Prints out the numbers 0,1,2,3,4
        print(x)

    for x in range(3, 6):       # Prints out 3,4,5
        print(x)

    for x in range(3, 8, 2):    # Prints out 3,5,7
        print(x)

    number = 0
    for times in range (1,5):
        print 'Sum: ', number + times

def forInList():
    primes = [2, 3, 5, 'Hi', 7]
    for prime in primes:
        print(prime)
    
    for letter in 'Python':     # Prints P-Y-T-H-O-N
        print 'Current Letter :', letter

if __name__ == "__main__":
    forInRange()
    forInList()
