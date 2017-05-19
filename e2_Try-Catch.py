#While True
#try catch
#break


def tryCatch():
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

def tryCatch2():
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except Exception, e:
            print(e)

if __name__ == "__main__":
    tryCatch2()

