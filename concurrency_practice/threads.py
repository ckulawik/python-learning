#!/usr/bin/env python
import threading
from time import sleep

def do_first():
    print("do_first running line 1")
    sleep(5)
    print("do_first running line 2")
    sleep(5)
    print("do_first running line 3")
    sleep(5)

def do_second():
    print("do_second running line 1")
    sleep(5)
    print("do_second running line 2")
    sleep(5)
    print("do_second running line 3")
    sleep(5)

def main():
    t1 = threading.Thread(target=do_first)
    t2 = threading.Thread(target=do_second)
    t1.start(), t2.start()

    t1.join(), t2.join()

if __name__ == "__main__":
    main()
