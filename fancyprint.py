import time

def fancy_print(string):
    for each in string:
        time.sleep(.1)
        print(each, end='')


tester = "This is a fairly long string of words. It's just to see if my theory is correct."

fancy_print(tester)