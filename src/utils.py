import psutil
import os


# --------------------
# System Usage
# --------------------
def get_cpu_usage():
    return psutil.cpu_percent()


def get_memory_usage():
    return psutil.virtual_memory().percent


def get_disk_usage():
    return psutil.disk_usage("/").percent


def get_ram_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024**2


def print_system_usage():
    print(f"CPU: {get_cpu_usage()}%")
    print(f"Memory: {get_memory_usage()}%")
    print(f"Disk: {get_disk_usage()}%")


def print_ram_usage():
    print(f"RAM: {get_ram_usage()} MB")
