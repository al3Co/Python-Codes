import time
import sys
from random import randint

def prueba():
    fps_t = 0
    fps_f = 0
    now1 = int(time.time())
    while  int(time.time()) < now1 +5:
        now = int(time.time())
        fps_f += 1
        if fps_t == 0:
            fps_t = now
            print fps_t
        elif fps_t < now:
            print '\rFPS: %.2f' % (1.0 * fps_f / (now-fps_t)),
            sys.stdout.flush()
            fps_t = now
            fps_f = 0
        time.sleep(randint(0,3))

def prueba2():
    print 'Random 0-3 flush'
    a = 0
    for i in range(3):
        print '\rNum: %.2f' % (randint(0,3)),
        sys.stdout.flush()
        a +=1
        time.sleep(1)
    print 'Finalizado'

prueba()
prueba2()
