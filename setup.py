import os
import requests
os.system("pip install psutil")
os.system("clear")
import time
print("""\033[0;37m
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⡀⠄⡀⠄⡀⠄⡀⢀⠄⡀⢀⠄⡀⠄⡀⠄⠄⠄⠄⢀⠄⠄⡀⢀⠄⠄⡀⠄⠄⠄⠄
    ⠄⠄⠄⠈⠄⠁⠈⠄⠂⠄⡀⠄⠄⡀⢀⠄⢀⠄⢀⠄⡀⠠⠄⠄⠂⠁⠈⡀⠄⠄⠁⠄⠄⠄⠂⠄⡀⠁⠄⠄
    ⠄⠄⠄⠁⠄⠁⠄⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠄⡀⡀⠄⠄⠁⢀⢁⠄⡀⠠⠄⠁⡈⢀⠈⢀⠠⠄⢀⠄⠄
    ⠄⠄⠄⠄⠁⠄⠁⠄⠂⠄⡠⣲⢧⣳⡳⡯⣟⣼⢽⣺⣜⡵⣝⢜⢔⠔⡅⢂⠄⠄⠁⠄⢀⠄⡀⠄⡀⠄⠄⠄
    ⠄⠄⠄⠄⠈⠄⠈⠄⢀⡇⡯⡺⢵⣳⢿⣻⣟⣿⣿⣽⢾⣝⢮⡳⣣⢣⠣⡃⢅⠂⠐⠈⠄⠄⢀⠄⡀⠄⠄⠄
    ⠄⠄⠄⠄⠈⠄⠐⢀⠇⡪⡸⡸⣝⣾⣻⣯⣿⣿⡿⣟⣿⡽⣗⡯⣞⢜⢌⠢⡡⢈⠈⠄⠁⠈⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠐⠄⠈⠆⠕⢔⠡⣓⣕⢷⣻⣽⣝⢷⣻⣻⣝⢯⢿⠹⠸⡑⡅⠕⠠⠠⠄⠅⠄⠂⠄⠂⠈⠄⠄⠄
    ⠄⠄⠄⠄⠄⠂⠡⡑⢍⠌⡊⢢⢢⢱⠼⣺⢿⢝⠮⢪⣪⡺⣘⡜⣑⢤⢐⠅⠡⢂⠡⠐⡀⢀⠠⠐⠄⠐⠄⠄
    ⠄⠄⠄⠄⢈⢀⠡⠨⡢⡑⡌⡔⡮⡷⣭⢧⣳⠭⣪⣲⣼⣾⣟⣻⣽⣺⣸⣜⢌⢆⢌⠐⠄⡀⠄⡀⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⠠⠄⠌⡢⡵⠺⠞⠟⠛⠯⠟⠟⠝⡫⢗⠟⠝⠙⠉⠊⠑⠉⠉⠉⠑⢒⠠⠁⠄⡀⠠⠄⠄⠄⠄
    ⠄⠄⠄⠐⡀⠄⠄⠅⡪⠄⠂⠄⠄⠄⠄⠄⠄⠄⢀⢕⢔⠄⠄⠄⠄⡀⠠⠐⠈⢀⠄⠠⠄⡁⠄⡀⠂⠠⠄⠄
    ⠄⠄⠄⠠⠄⠄⠂⡑⠄⠄⠠⠐⠄⠁⠄⠁⠄⠄⢸⣿⣿⡂⠄⠄⢀⠄⡀⠄⠂⠠⠐⠄⡐⡀⠂⢀⠐⠄⠄⠄
    ⠄⠄⠄⠄⢐⠄⠂⢕⢅⢄⠄⣀⡀⢄⠄⠁⣀⣔⡵⣿⣯⠧⡣⣢⡠⢀⢀⡠⠐⢀⢐⠠⢀⠐⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠐⡔⢀⠘⢽⣻⣶⣥⣉⠥⡣⣱⣷⠻⣪⣻⣷⡣⡣⢫⣞⣗⡦⡵⢻⠺⡸⠐⡀⠐⠄⠂⡀⠄⠄⠄
    ⠄⠄⠄⠄⠂⠘⡀⠔⢀⠑⠍⠍⡽⣽⣿⣻⠂⡷⣯⡿⣟⡿⠌⡆⠘⣾⣻⢵⢕⠔⢀⠁⠠⠈⡀⠁⠄⡀⠄⠄
    ⠄⠄⠄⠄⠠⠄⠄⡐⢰⢈⢄⠱⢽⣺⢳⠁⣈⠄⠄⠈⠊⠈⠄⠄⢡⣐⢫⢯⡢⢊⢄⢪⠨⠠⠄⡀⠁⠄⠄⠄
    ⠄⠄⠄⠄⠂⠄⠂⠠⠱⣕⡣⡇⡏⢮⢕⣸⣾⠠⠄⠄⠄⠂⠄⠄⠌⢟⣜⡵⣯⢷⡴⡅⠅⡂⠠⠄⢈⠄⠄⠄
    ⠄⠄⠄⠄⠂⠁⢀⠈⠌⡪⢝⢾⣝⣎⠒⠏⠙⠠⠑⠁⠆⠒⠐⠐⠉⢀⠑⣍⡿⣽⡽⡂⠕⠄⠄⠂⢀⠠⠄⠄
    ⠄⠄⠄⠐⠄⡈⠄⢀⠄⠊⠍⢯⣷⣏⢊⢀⣈⣠⣤⣤⣤⣴⣶⢶⣴⢤⢬⣌⢻⡺⡻⠈⠄⠂⠄⠂⡀⠄⠄⠄
    ⠄⠄⠄⠄⠂⢀⠐⠄⠄⠂⠡⠑⠕⠅⡕⡽⡑⡁⠉⠉⠉⠉⠁⠁⠁⠠⢊⠊⠢⠈⠄⠨⠄⠄⠁⠐⢀⠈⠄⠄
    ⠄⠄⠄⠈⢀⠄⠄⠈⡀⢂⠐⠄⠂⠁⠠⠁⡢⡪⣢⣲⣦⣖⡔⡤⡨⡐⢄⠌⠠⠈⠐⠄⠂⠠⠁⢈⠠⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⢂⠄⠢⠂⠈⡀⠈⡀⠈⠰⠹⡨⠑⡑⠕⠕⠊⠌⠌⠄⠐⠄⠂⠁⢈⠄⡁⠐⠄⡐⢀⠂⠄
    ⠄⠄⠄⠄⡐⢄⠑⠄⠄⡇⡁⠄⠄⠄⠄⡈⠄⠄⠄⠄⢀⠠⠄⠂⢀⠐⠄⡈⠠⠈⠄⠄⠠⠐⠄⠁⠠⠄⠄⠄
    ⠄⠄⡀⢊⠨⢀⢊⠄⠨⡂⡂⠄⠂⠄⢀⠄⠠⠄⠂⠄⠄⡀⠠⠄⠄⠄⠐⠄⠄⡀⠁⡀⠂⠄⠂⠁⠨⠄⠅⠄
    ⠄⠄⠐⠄⢂⠢⡀⠄⠬⠄⠂⠅⡀⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄⡀⠂⠄⠂⠄⢀⠄⠄⠄⠄⠂⠄⠂⢈⠐⠄⠄
    ⠄⠄⠈⡀⠄⠄⠄⠄⠅⠅⠐⠄⠄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠁⠄⠄⠄⠂⢐⠄⠐⠄
    ⠄⠄⠄⠄⠄⠂⠄⠄⠕⠈⡂⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠄⠄⠂⠄""")

time.sleep(3)
import os

hostname = os.uname()[1]
print("Hostname:", hostname)



import platform
import socket
import os
import subprocess
import psutil

# OS Information
os_info = platform.system() + " " + platform.release()
print("OS Information:", os_info)

# Hostname
hostname = socket.gethostname()
print("Hostname:", hostname)

# Uptime
uptime = os.popen("uptime -p").read().strip()
print("Uptime:", uptime)

# CPU Information
cpu_info = subprocess.check_output("lscpu | grep 'Model name'", shell=True).strip().decode().split(":")[1].strip()
print("CPU Info:", cpu_info)

# Memory Usage
memory_info = psutil.virtual_memory()
print("Memory Usage:", f"{memory_info.used / (1024 ** 2):.0f}MiB / {memory_info.total / (1024 ** 2):.0f}MiB")


import requests

def get_gce_metadata():
    try:
        response = requests.get('http://metadata.google.internal/computeMetadata/v1/instance/hostname', headers={'Metadata-Flavor': 'Google'})
        if response.status_code == 200:
            return "Google Compute Engine"
        else:
            return "Unknown"
    except requests.RequestException:
        return "Unknown"

host_info = get_gce_metadata()
print("Host:", host_info)

get_gce_metadata()



