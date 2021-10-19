

from multiprocessing import Process,Queue,Pool,Manager
import time
import os

def detailProcess():
    print(f'{os.getpgid()} --- {os.getppid()}')



if __name__ =='__main__':
    p = Process(target = detailProcess)
    p.start