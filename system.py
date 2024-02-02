import platform
import psutil

def get_system_info():
    # Operating system details
    os_info = {
        "System": platform.system(),
        "Version": platform.version(),
        "Release": platform.release(),
        "Architecture": platform.machine()
    }

    # CPU information
    
    cpu_info = {
        "Physical cores": psutil.cpu_count(logical=False),
        "Total cores": psutil.cpu_count(logical=True)
    }

    # RAM details
    ram_info = psutil.virtual_memory()
    ram_details = {
        "Total RAM": f"{ram_info.total / (1024 ** 3):.2f} GB",
        "Used RAM": f"{ram_info.used / (1024 ** 3):.2f} GB",
        "Free RAM": f"{ram_info.available / (1024 ** 3):.2f} GB"
    }

    return os_info, cpu_info, ram_details

def display_system_info():
    os_info, cpu_info, ram_details = get_system_info()

    print("Operating System Information:")
    for key, value in os_info.items():
        print(f"{key}: {value}")

    print("\nCPU Information:")
    for key, value in cpu_info.items():
        print(f"{key}: {value}")

    print("\nRAM Details:")
    for key, value in ram_details.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    display_system_info()
