import subprocess
import time
from datetime import datetime, time as dt_time, timedelta

# 定義啟動時間和關閉時間
start_time = dt_time(14, 56)
end_time = dt_time(17, 35)  # 7點17分
wait_time = 5
# 無窮迴圈以定時啟動和關閉應用程式
while True:
    current_time = datetime.now().time()
    print(current_time)
    # 檢查是否到達啟動時間
    if current_time >= start_time and current_time < end_time:
        app_name = "C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"
        process = subprocess.Popen(app_name)
        print(f"{app_name}已經啟動")
        time.sleep(wait_time)
        process.terminate()  # 或者使用 process.kill()，具體取決於你的需求

   
    time.sleep(10)
    # 檢查是否需要休眠，以免無限迴圈變得過於消耗資源
    # next_day = datetime.now() + timedelta(days=1)
    # next_start_time = datetime(next_day.year, next_day.month, next_day.day, start_time.hour, start_time.minute)
    # time_until_next_start = (next_start_time - datetime.now()).total_seconds()
    # time.sleep(time_until_next_start)

print('Schedule started ...')  # 這行不會被執行
input()