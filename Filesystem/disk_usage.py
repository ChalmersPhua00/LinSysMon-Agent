import shutil
import os

def disk_usage():
    print(f"{'Mount':<20} {'Size (GB)':<10} {'Free (GB)'}")
    print("-" * 45)
    mounts = []
    try:
        with open('/proc/mounts', 'r') as f:
            for line in f:
                parts = line.split()
                if len(parts) >= 2:
                    device, mountpoint = parts[0], parts[1]
                    if device.startswith('/dev/') or mountpoint == '/':
                        mounts.append(mountpoint)
    except FileNotFoundError:
        pass
    for mount in sorted(list(set(mounts))):
        try:
            usage = shutil.disk_usage(mount)
            size_gb = usage.total / (1024**3)
            free_gb = usage.free / (1024**3)
            print(f"{mount:<20} {size_gb:<10.2f} {free_gb:<10.2f}")
        except OSError:
            continue

if __name__ == "__main__":
    disk_usage()