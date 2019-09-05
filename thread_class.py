import threading
import time
from QM_se import get_info


exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # Put what you want to run here
        print("Starting " + self.name)
        get_info(self.name)
        # sleep minutes
        sleep_minutes = 60
        for i in range(sleep_minutes):
            time.sleep(60)
        print("Exiting " + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1