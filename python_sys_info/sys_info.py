# !/usr/bin/python
# -*- coding: UTF-8 -*-



from __future__ import print_function
import time

import psutil


class BaseMonitor(object):
    def __init__(self):
        self.data = {}

    def collect(self):
        # 打印日志、统计消耗的时间

        print('run {0} to collect monitor data'.format(self.__class__.__name__))
        start = time.time()

        self.do_work()

        elapsed = time.time() - start
        print('spend time on {0} to collect monitor data  is {1}'.format(self.__class__.__name__, elapsed))

    def do_work(self):
        raise NotImplementedError


class DiskMonitor(BaseMonitor):
    def do_work(self):
        disk_percent = psutil.disk_usage('/').percent
        disk_total = psutil.disk_usage('/').total / 1024 / 1024 / 1024.0
        self.data.update(dict(disk_percent=disk_percent,
                              disk_total=disk_total))


class MemoryMonitor(BaseMonitor):
    def do_work(self):
        """
        psutil.virtual_memory()
        svmem(total=4159041536, available=3723980800, percent=10.5, used=1599082496,
         free=2559959040, active=587403264, inactive=897105920, buffers=95989760, cached=1068032000)
        """
        memory_info = psutil.virtual_memory()
        memory_used = (memory_info.total * memory_info.percent / 100) / 1024 / 1024

        self.data.update(dict(memory_used=memory_used))


def main():
    disk_monitor = DiskMonitor()
    memory_monitor = MemoryMonitor()

    result = {}
    for obj in [disk_monitor, memory_monitor]:
        obj.collect()
        result.update(obj.data)

    print('*' * 80)
    print(result)


if __name__ == '__main__':
    main()
