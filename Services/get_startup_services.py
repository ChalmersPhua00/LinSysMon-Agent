import subprocess
import sys

def get_startup_services(limit):
    try:
        limit = int(limit)
        cmd = ["systemctl", "list-unit-files", "--type=service", "--state=enabled", "--no-pager", "--no-legend"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        lines = result.stdout.strip().splitlines()
        print(f"Automatic Startup Services (Enabled)\nLimit: {limit}")
        print(f"{'Unit File':<50} {'State':<15}")
        print("-" * 65)
        for i, line in enumerate(lines):
            if i >= limit:
                break
            parts = line.split()
            if len(parts) >= 2:
                print(f"{parts[0]:<50} {parts[1]:<15}")
    except Exception as e:
        print(f"Error getting startup services: {e}")

if __name__ == "__main__":
    limit = sys.argv[1]
    get_startup_services(limit)