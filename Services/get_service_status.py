import subprocess
import sys

def get_service_status(service_name):
    try:
        cmd = ["systemctl", "status", service_name, "--no-pager"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout
        if result.stderr:
            output += f"\nStderr:\n{result.stderr}"
            
        print(f"Service Status: {service_name}\n```\n{output.strip()}\n```")
    except Exception as e:
        print(f"Error getting status for {service_name}: {e}")

if __name__ == "__main__":
    get_service_status(sys.argv[1])