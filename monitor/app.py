# -*- coding: utf-8 -*-

import apscheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from app.LgbMenhuMonitor import LgbMenhuMonitor
from app.LgbMenhuMonitor import running

if __name__ == "__main__":
    monitor = LgbMenhuMonitor()
    scheduler = BlockingScheduler()
    scheduler.add_job(monitor.monitor_and_send_message, 'cron', second='*/5')
    try:
        scheduler.start()
    except KeyboardInterrupt, SystemExit:
        scheduler.shutdown()
