from mcp.server.fastmcp import FastMCP
import sys
import os
import subprocess
import io
import contextlib

# Add current directory to path to ensure we can import local modules
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
# Import local modules
from Process import list_processes as list_processes_module
from Filesystem import search_filesystem as search_filesystem_module
from Filesystem import find_large_files as find_large_files_module
from Filesystem import disk_usage as disk_usage_module
from Filesystem import list_directory as list_directory_module
from Filesystem import read_file as read_file_module
from Filesystem import file_metadata as file_metadata_module
from Filesystem import get_working_directory as get_working_directory_module
from Filesystem import change_working_directory as change_working_directory_module
from Services import get_service_details as get_service_details_module
from Services import get_service_status as get_service_status_module
from Services import find_service as find_service_module
from Services import get_running_services as get_running_services_module
from Services import get_startup_services as get_startup_services_module
from System import get_system_overview as get_system_overview_module
from System import get_hardware_info as get_hardware_info_module
from System import get_os_info as get_os_info_module
from System import get_environment_vars as get_environment_vars_module
from System import get_installed_software as get_installed_software_module
from System import get_system_uptime_info as get_system_uptime_info_module
from System import get_system_paths as get_system_paths_module
# Initialize FastMCP server
mcp = FastMCP("WinSysMon")

def capture_stdout(func, *args, **kwargs):
    """Helper to capture print output from existing functions"""
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        func(*args, **kwargs)
    return f.getvalue()

@mcp.tool()
def list_processes() -> str:
    """Lists current running processes."""
    return capture_stdout(list_processes_module.list_processes)

@mcp.tool()
def search_filesystem(pattern: str, path: str, recursive: bool) -> str:
    """Searches for files matching a pattern."""
    return capture_stdout(search_filesystem_module.search_filesystem, pattern, path, recursive)

@mcp.tool()
def find_large_files(path: str, size_threshold_mb: int) -> str:
    """Finds files larger than the specified threshold in MB."""
    return capture_stdout(find_large_files_module.find_large_files, path, size_threshold_mb)

@mcp.tool()
def disk_usage() -> str:
    """Retrieves disk usage information."""
    return capture_stdout(disk_usage_module.disk_usage)

@mcp.tool()
def list_directory(path: str, recursive: bool) -> str:
    """Lists directory contents."""
    return capture_stdout(list_directory_module.list_directory, path, recursive)

@mcp.tool()
def read_file(path: str) -> str:
    """Reads the content of a file."""
    return capture_stdout(read_file_module.read_file, path)

@mcp.tool()
def file_metadata(path: str) -> str:
    """Retrieves file metadata."""
    return capture_stdout(file_metadata_module.file_metadata, path)

@mcp.tool()
def get_working_directory() -> str:
    """Returns the current working directory (PWD)."""
    return capture_stdout(get_working_directory_module.get_working_directory)

@mcp.tool()
def change_working_directory(path: str) -> str:
    """Changes the current working directory (CD)."""
    return capture_stdout(change_working_directory_module.change_working_directory, path)

@mcp.tool()
def get_service_details(service_name: str) -> str:
    """Retrieves detailed information about a specific service."""
    return capture_stdout(get_service_details_module.get_service_details, service_name)

@mcp.tool()
def get_service_status(service_name: str) -> str:
    """Retrieves the current status of a specific service."""
    return capture_stdout(get_service_status_module.get_service_status, service_name)

@mcp.tool()
def find_service(search_term: str) -> str:
    """Searches for services by name or display name."""
    return capture_stdout(find_service_module.find_service, search_term)

@mcp.tool()
def get_running_services(limit: int) -> str:
    """Retrieves a list of currently running services."""
    return capture_stdout(get_running_services_module.get_running_services, limit)

@mcp.tool()
def get_startup_services(limit: int) -> str:
    """Retrieves services configured to start automatically."""
    return capture_stdout(get_startup_services_module.get_startup_services, limit)

@mcp.tool()
def get_system_overview() -> str:
    """Retrieves a high-level overview of the system (Hostname, OS, CPU, RAM, Uptime)."""
    return capture_stdout(get_system_overview_module.get_system_overview)

@mcp.tool()
def get_hardware_info(category: str) -> str:
    """Retrieves detailed hardware information. Category can be 'cpu', 'memory', 'disk', 'network', or 'all'."""
    return capture_stdout(get_hardware_info_module.get_hardware_info, category)

@mcp.tool()
def get_os_info() -> str:
    """Retrieves detailed Operating System information and recent hotfixes."""
    return capture_stdout(get_os_info_module.get_os_info)

@mcp.tool()
def get_environment_vars() -> str:
    """Retrieves environment variables."""
    return capture_stdout(get_environment_vars_module.get_environment_vars)

@mcp.tool()
def get_installed_software() -> str:
    """Retrieves a list of installed software via WMI."""
    return capture_stdout(get_installed_software_module.get_installed_software)

@mcp.tool()
def get_system_uptime_info() -> str:
    """Retrieves system uptime and last boot time information."""
    return capture_stdout(get_system_uptime_info_module.get_system_uptime_info)

@mcp.tool()
def get_system_paths() -> str:
    """Retrieves important system paths and the PATH environment variable."""
    return capture_stdout(get_system_paths_module.get_system_paths)

if __name__ == "__main__":
    mcp.run()