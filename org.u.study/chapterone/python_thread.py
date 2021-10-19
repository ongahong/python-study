
import threading
from threading import Thread,Lock
import time


# 协程是轻量级的线程，线程切换非常耗性能，协程切换只是单纯的操作CPU的上下文。
# 切换需要的资源最大的：进程
# 切换需要的资源一般的：线程
# 切换需要的资源最小的：协程

# 使用场景：
# 1.多进程适合CPU密集型操作（如计算密集型）
# 2.多线程适合IO密集型（读写数据操作比较多的），如涉及到网络、磁盘IO的任务都是IO密集型
# 3. 协程适用于IO阻塞且需要大量并发的场景
# 4. CPU+IO密集型：多进程+协程



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



def eat() :
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