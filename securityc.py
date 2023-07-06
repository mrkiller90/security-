import time
import os
def delete_blocked_ips():
    command = 'iptables -L INPUT -v -n | awk \'!/^$|Chain|pkts/ {print $1" "$2" "$8}\''
    output = os.popen(command).read()
    lines = output.strip().split('\n')
    for line in lines:
        fields = line.split()
        ip = fields[1]
        packets = int(fields[2])
        if packets > 2000:
            os.system('iptables -D INPUT -s ' + ip + ' -j DROP')
while True:
	try:
        os.system("sudo killall -u f4cabs & deluser f4cabs")
        os.system("sudo killall -u s & deluser s")
        os.system("sudo killall -u meo092t & deluser meo092t")
        delete_blocked_ips()
        time.sleep(300)
    except:
    	os.system("Script Is Running.... Dont Worry ;)")