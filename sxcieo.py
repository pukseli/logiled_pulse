from multiprocessing import Process
import time

def loop_a():
    a = 0
    while 1:

        print("a")
        time.sleep(.5)
        if a== 10:
            Process(target=loop_b).start()
            a = 0
        else:
            a = a+1

def loop_b():
    for a in range(5):
        time.sleep(0.5)
        print("b" + str(a))

if __name__ == '__main__':
    Process(target=loop_a).start()
