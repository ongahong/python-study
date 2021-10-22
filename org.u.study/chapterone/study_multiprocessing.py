

from multiprocessing import Process,Queue,Pool,Manager
import time
import os

def detailProcess():
    print(f'{os.getpid()} --- {os.getppid()}')



if __name__ =='__main__':
    print('进程start')
    p = Process(target=detailProcess)
    p.start
    print('进程end')