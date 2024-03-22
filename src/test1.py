import datetime
import os
import platform
import psutil
import random
import socket
import sys
import time

def print_os_info():
    print("OS Information:")
    print(f"System: {platform.system()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Processor: {platform.processor()}")
    print()

def print_system_stats(args):
    print("System Stats:")
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    cpu_count = psutil.cpu_count()
    boot_time = psutil.boot_time()

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print()

    dump_output_files(cpu_usage, memory_usage, cpu_count, boot_time, args)

def dump_output_files(cpu_usage, memory_usage, cpu_count, boot_time, args):
    print("Dumping output files with system stats...")
    
    label = socket.gethostname() if not len(args) else args[0]
    ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
    cpu_log = f"{label}_cpu_usage_{ts}.log"
    memory_log = f"{label}_memory_usage_{ts}.log"
    other_results_dir = f"other_results_{label}_{ts}"
    cpu_log2 = os.path.join(other_results_dir, f"{label}_cpu_count_{ts}.log")
    boot_time_log = os.path.join(other_results_dir, "boot_results", f"{label}_boot_time_{ts}.log")
    
    os.makedirs(f"{other_results_dir}/boot_results/")
    
    os.system(f"echo {cpu_usage} > {cpu_log}")
    os.system(f"echo {memory_usage} > {memory_log}")
    os.system(f"echo {cpu_count} > {cpu_log2}")
    os.system(f"echo {boot_time} > {boot_time_log}")
    
    print(f"Collect CPU Usage log: {os.path.abspath(cpu_log)}")
    print(f"Collect Memory Usage log: {os.path.abspath(memory_log)}")
    print(f"Collect other_results dir: {os.path.abspath(f'{other_results_dir}/')}")
    print()

def main(sleep_time, args):
    print("Hello, world!")

    print_os_info()
    print(f"sleeping for {sleep_time}")
    time.sleep(sleep_time)

    print_system_stats(args)

if __name__ == "__main__":
    sleep_time = random.randint(4, 20)  
    main(sleep_time, sys.argv[1:])

