import time
import math
start_time = time.time()

def main():
    try:
        print "hello world1"
        time.sleep(5)
        print "hello world2"
    except KeyboardInterrupt, e:
        print
        print "ManualControlException"

def fixedTime():
    new_time = (((int(math.floor(start_time)) + 1) / 10) + 1) * 10
    print("Wait %s seconds ..." % (new_time - start_time))
    time.sleep(new_time - start_time)
    main()

if __name__ == "__main__":
    fixedTime()
