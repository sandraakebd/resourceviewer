import psutil
import time
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display_resource_usage():
    clear_console()
    print("Resource Viewer - Real-time System Resource Usage")
    print("=" * 50)

    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

    # Get memory usage
    memory_info = psutil.virtual_memory()
    print(f"Memory Usage: {memory_info.percent}% ({memory_info.used / (1024 ** 3):.2f} GB / {memory_info.total / (1024 ** 3):.2f} GB)")

    # Get disk usage
    disk_info = psutil.disk_usage('/')
    print(f"Disk Usage: {disk_info.percent}% ({disk_info.used / (1024 ** 3):.2f} GB / {disk_info.total / (1024 ** 3):.2f} GB)")

def main():
    try:
        while True:
            display_resource_usage()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting Resource Viewer.")

if __name__ == "__main__":
    main()