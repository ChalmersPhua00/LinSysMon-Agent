import subprocess
import sys

def find_service(search_term):
    try:
        cmd = ["systemctl", "list-units", "--type=service", "--all", "--no-pager", "--full"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        lines = result.stdout.splitlines()
        matches = []
        if lines:
            matches.append(lines[0])
        for line in lines[1:]:
            if search_term.lower() in line.lower():
                matches.append(line)
        print(f"Search term: \"{search_term}\"\n```\n" + "\n".join(matches) + "\n```")
    except Exception as e:
        print(f"Error searching services: {e}")

if __name__ == "__main__":
    find_service(sys.argv[1])