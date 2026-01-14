import subprocess

def list_processes():
    print(f"{'PID':<10} {'Name':<30} {'PPID':<20} {'CommandLine'}")
    print("-" * 90)
    try:
        cmd = ['ps', '-eo', 'pid,comm,ppid,args', '--no-headers']
        result = subprocess.run(cmd, capture_output=True, text=True)
        for line in result.stdout.splitlines():
            parts = line.split(None, 3)
            if len(parts) < 4:
                continue
            pid, name, ppid, cmd_line = parts[0], parts[1], parts[2], parts[3]
            if len(cmd_line) > 40:
                cmd_line = cmd_line[:37] + "..."
            print(f"{pid:<10} {name:<30} {ppid:<20} {cmd_line}")
    except Exception as e:
        print(f"Error listing processes: {e}")

if __name__ == "__main__":
    list_processes()