import threading
import time

def say_hello(message1, message2):
    while True:
        print("hello" + message1 + message2)
        time.sleep(1)
def say_hi(message):
    while True:
        print("hi "+ message)
        time.sleep(1)
hello_thread = threading.Thread(target= say_hello, args=("arg1", "arg2"))
hi_thread = threading.Thread(target= say_hi, args=("arg1",)) # note, we need to add , in args

hello_thread.start()
hi_thread.start()