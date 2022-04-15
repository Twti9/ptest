#!/usr/bin/env python
# -*- coding:utf-8 -*-
#开发时间：2022/4/15 14:01
import time
import queue
import threading
def worker(i):
    while True:
        item = q.get()
        if item is None:
            print("线程%s发现了一个None，可以休息了"%i)
            break
        time.sleep(0.5)
        print('线程%s完成了任务%s'%(i,item))
        q.task_done()
if __name__ == '__main__':
    num_of_threads=5
    source = [i for i in range(1, 21)]
    q=queue.Queue()
    threads=[]
    for i in range(1,num_of_threads+1):
        t=threading.Thread(target=worker,args=(i,))
        threads.append(t)
        t.start()
    for item in source:
        time.sleep(0.5)
        q.put(item)
    q.join()
    for i in range(num_of_threads):
        q.put(None)
    for t in threads:
        t.join()
    print(threads)

