import subprocess
import sys

def get_service_details(service_name):
    try:
        # Basic Info (Status)
        cmd_status = ["systemctl", "status", service_name, "--no-pager"]
        basic_info = subprocess.run(cmd_status, capture_output=True, text=True).stdout
        # Extended Info (Properties)
        cmd_show = ["systemctl", "show", service_name, "--no-pager"]
        info = subprocess.run(cmd_show, capture_output=True, text=True).stdout
        # Dependencies
        cmd_dep = ["systemctl", "list-dependencies", service_name, "--no-pager"]
        dependencies = subprocess.run(cmd_dep, capture_output=True, text=True).stdout
        print(f"Service Details: {service_name}\n")
        print(f"Basic Information\n```\n{basic_info.strip()}\n```\n")
        print(f"Extended Information\n```\n{info.strip()}\n```\n")
        print(f"Dependencies\n```\n{dependencies.strip()}\n```")
    except Exception as e:
        print(f"Error getting details for {service_name}: {e}")

if __name__ == "__main__":
    get_service_details(sys.argv[1])