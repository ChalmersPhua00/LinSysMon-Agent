import subprocess
import platform
import psutil
import time
import os

def format_bytes(size):
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    return f"{size:.2f} {power_labels[n]}"

def format_uptime(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{int(days)}d {int(hours)}h {int(minutes)}m {int(secs)}s"

def get_system_overview():
    try:
        uptime_seconds = time.time() - psutil.boot_time()
        os_info = "Linux"
        if os.path.exists("/etc/os-release"):
            with open("/etc/os-release") as f:
                for line in f:
                    if line.startswith("PRETTY_NAME="):
                        os_info = line.split("=")[1].strip().strip('"')
                        break
        print(f"-Hostname: {platform.node()}")
        print(f"-OS: {os_info}")
        print(f"-Kernel: {platform.release()}")
        print(f"-Architecture: {platform.machine()}")
        print(f"-CPU Cores: {psutil.cpu_count()}")
        print(f"-Total Memory: {format_bytes(psutil.virtual_memory().total)}")
        print(f"-Free Memory: {format_bytes(psutil.virtual_memory().available)}")
        print(f"-System Uptime: {format_uptime(uptime_seconds)}")
    except Exception as e:
        print(f"Error getting system overview: {e}")

if __name__ == "__main__":
    get_system_overview()