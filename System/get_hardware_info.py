import subprocess
import sys

def get_hardware_info(category):
    try:
        if category == "all" or category == "cpu":
            print("CPU Information")
            print("```")
            subprocess.run(["lscpu"], text=True)
            print("```\n")
        if category == "all" or category == "memory":
            print("Memory Information")
            print("```")
            subprocess.run(["free", "-h"], text=True)
            print("```\n")
        if category == "all" or category == "disk":
            print("Disk Information")
            print("```")
            subprocess.run(["lsblk", "-o", "NAME,SIZE,TYPE,MOUNTPOINT"], text=True)
            print("```\n")
        if category == "all" or category == "network":
            print("Network Adapters")
            print("```")
            subprocess.run(["ip", "-br", "addr"], text=True)
            print("```")
    except Exception as e:
        print(f"Error getting hardware info: {e}")

if __name__ == "__main__":
    get_hardware_info(sys.argv[1])