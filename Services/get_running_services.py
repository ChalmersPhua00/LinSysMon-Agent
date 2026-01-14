import subprocess
import sys

def get_running_services(limit):
    try:
        limit = int(limit)
        cmd = ["systemctl", "list-units", "--type=service", "--state=running", "--no-pager", "--no-legend"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        lines = result.stdout.strip().splitlines()
        print(f"Running Services\nLimit: {limit}")
        print(f"{'Name':<40} {'Status':<10} {'DisplayName'}")
        print("-" * 80)
        for i, line in enumerate(lines):
            if i >= limit:
                break
            parts = line.split(None, 4)
            if len(parts) >= 5:
                print(f"{parts[0]:<40} {parts[3]:<10} {parts[4]}")
    except Exception as e:
        print(f"Error getting running services: {e}")

if __name__ == "__main__":
    limit = sys.argv[1]
    get_running_services(limit)