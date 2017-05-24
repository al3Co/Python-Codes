# While condition
# While True

def whileCondition():
    count = 0
    while count < 5:
        print(count)
        count += 1  # This is the same as count = count + 1

def example1():
    count = 0
    while count < 5:
        print(count)
        count += 1  # This is the same as count = count + 1
        if count == 3:
            break

def example2():
    while True:
        try:
            x = int(raw_input("Please enter a Integer 1: "))
            y = int(raw_input("Please enter a Integer 2: "))
            print 'Sum = ', str(x + y)
            break
        except (ValueError), e:
            print 'Invalid number try again, error:', e

if __name__ == "__main__":
    whileCondition()

