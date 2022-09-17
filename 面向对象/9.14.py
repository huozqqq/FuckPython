import time
from time import sleep
class Clock(object):
    def __init__(self,hour,min,sec):
        self.hour=hour
        self.min=min
        self.sec=sec
    def move(self):
        self.sec+=1
        if self.sec == 60:
            self.sec=0
            self.min+=1
            if self.min == 60 :
                self.min=0
                self.hour+=1
                if self.hour==24:
                    self.hour=0
    def show(self):
        return '%02d:%02d:%02d'% (self.hour,self.min,self.sec)

def main():
    print(111111)
    clock= Clock(23,59,50)
    while True:
        print(clock.show())
        sleep(1)
        clock.move()


if __name__ == '__main__':
    main()
