# An IP sweeping Python script is typically used to identify active hosts (devices) on a network by scanning a range of IP addresses to see which ones respond. The purpose is often to gather network information for system administration, inventory, or cybersecurity tasks.

# add ascii to display IP Sweeper
ip_sweeper = '''
 _                                                       
(_)                                                      
 _  _ __    ___ __      __  ___   ___  _ __    ___  _ __ 
| || '_ \  / __|\ \ /\ / / / _ \ / _ \| '_ \  / _ \| '__|
| || |_) | \__ \ \ V  V / |  __/|  __/| |_) ||  __/| |   
|_|| .__/  |___/  \_/\_/   \___| \___|| .__/  \___||_|   
   | |                                | |                
   |_|                                |_|                    
'''
print(ip_sweeper)

# import modules
import subprocess  # this module lets you run commands
import platform  # to detect which OS i am on

# detect the OS
if platform.system().lower == "windows":
    para = "-n"
else:
    para = "-c"

# Base IP range (you can change this to match your own network)
base_ip = "192.168.1."
start = 1
end = 10

# loop through Ips
for ip in range(start, end + 1):
    ip = base_ip + str(ip)
    print(ip)

# run the command
result = subprocess.run(["ping", para, "1", ip], stdout=subprocess.DEVNULL)
if result.returncode == 0:
    alive_ips.append(ip)
    print(f"[+] {ip} is alive")
else:
    print(f"[-] {ip} is not responding")
