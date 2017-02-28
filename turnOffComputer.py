
import sys
import os
import time

def shutdown():
    try:
        cantidad = float(input('Ingresa tiempo en minutos: '))
        cantidad = cantidad * 60
        print 'Programado para ' + str(cantidad) + ' segundos'
        for x in range(0, int(cantidad)):
            print '\rShuting down in : %.2f' % (int(cantidad) - x),
            sys.stdout.flush()
            time.sleep(1)
        print'Bye'
        #os.system("shutdown -h now")
    except (RuntimeError, TypeError, NameError, SyntaxError):
        print('Oops!  That was no valid number.  Try again...')

if __name__ == "__main__":
    shutdown()
