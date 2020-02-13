import time
import subprocess as sp


# sleeps then opens file
def sleeper():
    i = 0
    while i < 10:  # number of times to open
        time.sleep(0.2)  # time between open file
        sp.Popen("pop_up.py", shell=True)
        i += 1


if __name__ == "__main__":
    sleeper()
