import subprocess
import time

# 應用程式的名稱
app_name = "C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"

# 等待幾秒後關閉應用程式
wait_time = 10  # 這裡的數字代表等待秒數

# 開始執行應用程式
process = subprocess.Popen(app_name)

# 等待一段時間
time.sleep(wait_time)

# 關閉應用程式
process.terminate()  # 或者使用 process.kill()，具體取決於你的需求