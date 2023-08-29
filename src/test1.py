import time
import random
import psutil
import platform
import os

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

    dump_output_files(cpu_usage, memory_usage)

def dump_output_files(cpu_usage, memory_usage):
    print("Dumping output files with system stats...")
    cpu_log = "cpu_usage.log"
    memory_log = "memory_usage.log"
    
    os.system(f"echo {cpu_usage} > {cpu_log}")
    os.system(f"echo {memory_usage} > {memory_log}")
    
    print(f"Collect CPU Usage log: {cpu_log}")
    print(f"Collect Memory Usage log: {memory_log}")
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

