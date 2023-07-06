import time
import subprocess

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

    time.sleep(300)
    print("Script Is Running.... Dont Worry ;)")
