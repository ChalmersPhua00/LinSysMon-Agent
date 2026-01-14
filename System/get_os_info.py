import subprocess
import os

def get_os_info():
    try:
        info_parts = []
        hostname = subprocess.run(["hostname"], capture_output=True, text=True).stdout.strip()
        info_parts.append(f"Hostname: {hostname}")
        if os.path.exists("/etc/os-release"):
            with open("/etc/os-release") as f:
                for line in f:
                    if line.startswith("PRETTY_NAME="):
                        info_parts.append(f"OS: {line.split('=')[1].strip().strip('\"')}")
                        break
        uname = subprocess.run(["uname", "-r"], capture_output=True, text=True).stdout.strip()
        info_parts.append(f"Kernel: {uname}")
        uptime = subprocess.run(["uptime", "-p"], capture_output=True, text=True).stdout.strip()
        info_parts.append(f"Uptime: {uptime}")
        print(f"System Details\n```\n" + "\n".join(info_parts) + "\n```")
    except Exception as e:
        print(f"Error getting OS info: {e}")

if __name__ == "__main__":
    get_os_info()