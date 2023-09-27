# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
#os.system(r'C:\Users\savin\Nox_share\ImageShare\FateGO.apk')
#os.system(r'D:\LDPlayer\LDPlayer9\dnplayer.exe')

import time
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def job1():
    print(f'FGO主帳啟動: 目前時間{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    os.system(r'C:\Users\savin\Nox_share\ImageShare\FateGO.apk')
def job2():
    print(f'FGO小帳啟動: 目前時間{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    os.system(r'D:\LDPlayer\LDPlayer9\dnplayer.exe')
    
# 指定時區（一定要指定，否則會失敗）
scheduler = BlockingScheduler(timezone="Asia/Shanghai")


# 每週一到日的上午5點51分執行job1函式
scheduler.add_job(job1, 'cron', day_of_week='0-6', hour=5, minute=51 )

scheduler.add_job(job2, 'cron', day_of_week='0-6', hour=6, minute=51 )

scheduler.start()

print('Schedule started ...')  # 這行不會被執行
input()