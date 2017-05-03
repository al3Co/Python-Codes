import time

file = time.strftime("%Y%m%d-%H%M%S")
print 'Code to save data to a file named:', file

def main():
    while True:
        while True:
            try:
                airSpeed = int(input('Entry air speed (km/h): '))
                ampere = int(input('Entry Ampere (A): '))
                resistence = int(input('Entry Resistance (Ohm): '))
                break
            except (NameError, ValueError, SyntaxError) as err:
                print 'Oops!  That was no valid number.  Try again...', err
                pass
        if (airSpeed == 0 & ampere == 0 & resistence == 0):
            break
        try:
    	   f = open(file,'a')
    	   f.write(str(airSpeed)+'\t'+ str(ampere)+'\t'+ str(resistence)+'\t'+ str(ampere*resistence)+'\n')
    	   f.close()
           print 'Air Speed', airSpeed, 'Current', ampere, 'Resistance', resistence, 'Voltage', (ampere*resistence), ' Saved' 
        except OSError as err:
            print("OS error: {0}".format(err))
    print ('Close')

if __name__ == "__main__":
    main()

