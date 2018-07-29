import threading
import random
import logging
logging.basicConfig(level=logging.INFO,format="%(thread)d %(threadName)s %(message)s",filename='F:/test.log')

class Dispatcher:
    def __init__(self,x = 0,num=0):
        self.data = x
        self.cond = threading.Condition()
        self.event = threading.Event()
        self.num = num
        self.count = 0

    def produce(self):
        data = random.randint(1,20)
        for i in range(self.num):
            with self.cond:
                self.data = data
                self.cond.notify(1)

            self.event.wait(1)

    def custom(self):
        sum = 0
        while True:
            with self.cond:
                self.cond.wait()
                sum += self.data
                self.count += 1
                if self.count == self.num:
                    logging.info("the result is {}".format(sum))
                    print("run sucess")

d = Dispatcher(0,10)
threading.Thread(target=d.custom).start()
threading.Thread(target=d.produce).start()
