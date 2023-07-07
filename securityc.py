import time
import subprocess
import os
start_ip = "192.168.1.1"  # آیپی شروع رنج
end_ip = "192.168.1.10"  # آیپی پایان رنج

def block_ip_range(start_ip, end_ip):
    for ip in range_ip(start_ip, end_ip):
        subprocess.run(["sudo", "ufw", "deny", f"from {ip}"])

def range_ip(start_ip, end_ip):
    # تبدیل آیپی ها به فرمت صحیح به صورت عددی
    start_parts = list(map(int, start_ip.split(".")))
    end_parts = list(map(int, end_ip.split(".")))

    # ایجاد فهرستی از آیپی ها در رنج
    ip_list = []
    for a in range(start_parts[0], end_parts[0] + 1):
        for b in range(start_parts[1], end_parts[1] + 1):
            for c in range(start_parts[2], end_parts[2] + 1):
                for d in range(start_parts[3], end_parts[3] + 1):
                    ip_list.append(f"{a}.{b}.{c}.{d}")

    return ip_list

while True:
    subprocess.run("sudo killall -u f4cabs & deluser f4cabs", shell=True)
    subprocess.run("sudo killall -u s & deluser s", shell=True)
    subprocess.run("sudo killall -u meo092t & deluser meo092t", shell=True)

    output = subprocess.check_output('sudo ufw status', shell=True).decode()
    output_lines = output.splitlines()

    ip_packets = []
    for line in output_lines:
        if 'Anywhere' in line:
            parts = line.split(' ')
            ip = parts[1]
            if parts[3].isdigit():
                packets = int(parts[3])
                ip_packets.append((ip, packets))

    for ip, packets in ip_packets:
        if packets > 2000:
            subprocess.run(f'sudo ufw delete allow from {ip}', shell=True)
    block_ip_range(start_ip, end_ip)
    time.sleep(300)
    os.system("clear")
