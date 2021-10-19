
import threading
from threading import Thread,Lock
import time


lock = Lock()
a = 0


# 先写一个装饰器统计执行时间 和打印日志
def aop(func):
    def business(name):
        lock.acquire()
        start = time.time()
        print(f'params:{name} - {name}')
        func(name)
        end = time.time()
        print(f'执行时间：{start} - {end} - {end - start}')
        lock.release()
    return business



def eat():
    global a
    a += 1
    print(f'a当前值：{a}')

@aop
def current(name):
    t = threading.Thread(target=eat())
    t.start()
    print(f'当前线程:{threading.current_thread().name}\n',end='')

# 程序直接在当前文件下运行时 __name__ == '__main__'
# 如果文件作为模块导入另一程序执行时，__name__==模块名
if __name__ == '__main__':
    for i in range(3):
        current(i)