import time
import os
import subprocess
while True:
    os.system("sudo killall -u f4cabs & deluser f4cabs")
    os.system("sudo killall -u s & deluser s")
    os.system("sudo killall -u meo092t & deluser meo092t")
    command = "netstat -anp | grep 'tcp\|udp' | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort"
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    if output:
        lines = output.decode().split("\n")
        for line in lines:
            if line:
                count, ip = line.strip().split()
                count = int(count)
                if count > 2000:
                    delete_command = f"route delete {ip}"
                    delete_p = subprocess.Popen(delete_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    delete_output, delete_error = delete_p.communicate()
                    if delete_output:
                        print(delete_output.decode())
                    if delete_error:
                        print(delete_error.decode())
    else:
        print("There was an error running the command.")

    time.sleep(300)
    os.system("Script Is Running.... Dont Worry ;)")
