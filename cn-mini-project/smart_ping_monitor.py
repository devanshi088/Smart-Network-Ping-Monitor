from ping3 import ping
from datetime import datetime
import time
import csv
from colorama import Fore, Style

# List of devices to monitor
devices = ["8.8.8.8", "1.1.1.1", "192.168.1.1"]  # you can edit these IPs

# Create a CSV log file
with open("ping_log.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "IP Address", "Status", "Response Time (ms)"])

print("🔍 Smart Network Ping Monitor Started...\n")

# Continuous monitoring
while True:
    for ip in devices:
        response_time = ping(ip, timeout=2)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if response_time:
            print(Fore.GREEN + f"[{timestamp}] {ip} is ONLINE ({round(response_time*1000)} ms)" + Style.RESET_ALL)
            status = "Online"
            resp = round(response_time * 1000, 2)
        else:
            print(Fore.RED + f"[{timestamp}] {ip} is OFFLINE ❌" + Style.RESET_ALL)
            status = "Offline"
            resp = "N/A"

        # Write data to CSV
        with open("ping_log.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, ip, status, resp])

    # Wait 10 seconds before next check
    time.sleep(10)
