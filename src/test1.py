import time
import random
import psutil
import platform

def print_os_info():
    print("OS Information:")
    print(f"System: {platform.system()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Processor: {platform.processor()}")
    print()

def print_system_stats():
    print("System Stats:")
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print()

def main(sleep_time):
    print("Hello, world!")

    print_os_info()
    print(f"sleeping for {sleep_time}")
    time.sleep(sleep_time)

    print_system_stats()

if __name__ == "__main__":
    sleep_time = random.randint(4, 20)  
    main(sleep_time)

