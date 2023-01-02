#!/usr/bin/env python
from time import sleep
SLEEP_TIME = 20

def do_first() -> None:
    print(f"sleeping for {SLEEP_TIME} seconds")
    sleep(SLEEP_TIME)
    print("Done sleeping!")

def do_second() -> None:
    print("Just printing in this one")

def main() -> None:
    do_first()
    do_second()

if __name__ == "__main__":
    main()
