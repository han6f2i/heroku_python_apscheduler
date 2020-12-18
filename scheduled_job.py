#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

print('Hello Python')

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour='0,23', minute='*/2')
def scheduled_job():
    print(datetime.datetime.now())

sched.start()