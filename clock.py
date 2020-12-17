#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
# import urllib
import datetime
import requests

# target_url = "https://apscheduler.readthedocs.io/en/3.0/"
print('Hello Python')
# res = requests.get(target_url)
# print(res.text)

# 宣告一個排程
sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour='8-22', minute='*/20')
def scheduled_job():
    target_url = "https://han-huang.herokuapp.com/home/books/"
    res = requests.get(target_url)
    print(datetime.datetime.now())

sched.start()