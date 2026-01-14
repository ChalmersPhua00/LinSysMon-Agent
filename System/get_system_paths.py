import os

def get_system_paths():
    try:
        path_info = {
            "Home": os.environ.get("HOME", "N/A"),
            "User": os.environ.get("USER", "N/A"),
            "Shell": os.environ.get("SHELL", "N/A"),
            "Temp": "/tmp",
            "Config": "/etc",
            "Binaries": "/usr/bin"
        }
        path_env = os.environ.get("PATH", "").split(':')
        path_env_display = "\n".join(path_env[:20]) if path_env else "N/A"
        print("Important Directories")
        for key, value in path_info.items():
            print(f"- {key}: {value}")
        print(f"\nPATH Environment (First 20 entries)\n```\n{path_env_display}\n```")
    except Exception as e:
        print(f"Error getting system paths: {e}")

if __name__ == "__main__":
    get_system_paths()