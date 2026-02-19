###program

##thread is a unit opf excution winthin a program

##multithreading


# import threading

# import time

# def main():
#     for i in range(1,6):
#         time.sleep(2)
#         print(i)
# def main2():
#     time.sleep(2)
#     for i in range(1,6):
#         print(i)

# t1 = threading.Thread(target=main)
# t2 = threading.Thread(target=main2)

# t = time.time()

# ##start the thread

# t1.start()
# t2.start()

# ##joint the threads

# t1.join()
# t2.join()

# finished_time = time.time()-t

# print(finished_time)

from concurrent.futures import ThreadPoolExecutor

import time

def main():
    for i in range(1,6):
        time.sleep(2)
        print(i)

numbers = [1,2,3,4,5]

with ThreadPoolExecutor(max_workers=1) as executor:
    result  = executor.map(main1,numbers)
    