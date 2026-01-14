import subprocess
import shutil

def get_installed_software():
    try:
        # Try dpkg (Debian/Ubuntu)
        if shutil.which("dpkg"):
            cmd = "dpkg-query -W -f='${Package} ${Version}\n' | head -n 20"
            print("Installed Packages (Top 20 via dpkg):")
            subprocess.run(cmd, shell=True, text=True)
        # Try rpm (RHEL/CentOS/Fedora)
        elif shutil.which("rpm"):
            cmd = "rpm -qa --qf '%{NAME} %{VERSION}\n' | head -n 20"
            print("Installed Packages (Top 20 via rpm):")
            subprocess.run(cmd, shell=True, text=True)
        # Try pacman (Arch)
        elif shutil.which("pacman"):
            cmd = "pacman -Q | head -n 20"
            print("Installed Packages (Top 20 via pacman):")
            subprocess.run(cmd, shell=True, text=True)
        else:
            print("No supported package manager found (dpkg, rpm, pacman).")
    except Exception as e:
        print(f"Error getting installed software: {e}")

if __name__ == "__main__":
    get_installed_software()