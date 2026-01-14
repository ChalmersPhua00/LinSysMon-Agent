import os
import sys

def get_environment_vars():
    try:
        print(f"{'Variable':<30} {'Value'}")
        print("-" * 80)
        for key, value in sorted(os.environ.items()):
            # Truncate long values for display
            if len(value) > 50:
                value = value[:47] + "..."
            print(f"{key:<30} {value}")
    except Exception as e:
        print(f"Error getting environment variables: {e}")

if __name__ == "__main__":
    get_environment_vars()