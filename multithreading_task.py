from threading import Thread
import time

'''
Написати Python-скрипт, який створює чотири потоки.
Кожен потік повинен викликати функцію,
яка виводить в стандартний потік виведення послідовність рядків, переданих у функцію у вигляді аргументу
'''

arr = ["a", "b", "c", "d", "e"]


def logging_func(name):
    print("Thread {0} started\n".format(name))
    time.sleep(2)
    print("Thread {0} finished\n".format(name))


threads = list()
for i in range(4):
    t1 = Thread(target=logging_func, args=arr[i])
    threads.append(t1)
    t1.start()
    t1.join()
