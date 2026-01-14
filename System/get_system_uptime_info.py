import subprocess
import time
import psutil
import datetime

def format_uptime(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{int(days)}d {int(hours)}h {int(minutes)}m {int(secs)}s"

def get_system_uptime_info():
    try:
        boot_timestamp = psutil.boot_time()
        boot_time_str = datetime.datetime.fromtimestamp(boot_timestamp).strftime("%Y-%m-%d %H:%M:%S")
        uptime_seconds = time.time() - boot_timestamp
        # Get last boot info via standard linux command
        last_boot = subprocess.run(["who", "-b"], capture_output=True, text=True).stdout.strip()
        print(f"Current Uptime: {format_uptime(uptime_seconds)}")
        print(f"Boot Time: {boot_time_str}")
        print(f"System Boot Info: {last_boot}")
    except Exception as e:
        print(f"Error getting system uptime: {e}")

if __name__ == "__main__":
    get_system_uptime_info()