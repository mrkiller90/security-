import os
import subprocess
import time
import fileinput
import re
os.system("clear")
print("Mr Killer Script ! @Mr_Killer_1\n")
portt = input("Enter Your port from ssh : ")
portp = input("Enter Your panel port(default : 8081) : ")
udpp = input("Enter Your Udpw port(default : 7300) : ")
bannert = input("Enter Your banner Text : ")
#دیلیت کاربر نفوذی
os.system("sudo killall -u f4cabs & deluser f4cabs")
os.system("sudo killall -u s & deluser s")
os.system("sudo killall -u meo092t & deluser meo092t")
#رمزنگاری ssh
def replace_line(filepath, pattern, replacement):
    for line in fileinput.input(filepath, inplace=True):
        updated_line = re.sub(pattern, replacement, line)
        print(updated_line, end='')
sshd_config_file = '/etc/ssh/sshd_config'
pattern = r'^# Ciphers and keying'
replacement = 'Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes256-ctr'
def check_line(filepath, pattern):
    for line in fileinput.input(filepath):
        if re.search(pattern, line):
            return True
    return False
if not check_line(sshd_config_file, replacement):
    replace_line(sshd_config_file, pattern, replacement)

#تنظیم متن بنر 
f = open("/root/banner.txt", "a+")
f.write(bannert)
f.close()
#فعالسازی فایروال
os.system("sudo ufw reset")
time.sleep(4)
os.system("ufw allow 80")
os.system("ufw allow 443")
os.system("ufw allow default deny incoming")
os.system("sudo ufw default allow outgoing")
os.system("sudo ufw allow ssh")
os.system("ufw allow"+" "+portp)
os.system("ufw allow"+" "+portt)
os.system("ufw allow"+" "+udpp)
os.system("sudo ufw enable")
time.sleep(4)
#بستن رنج آیپی های خصوصی
"""
os.system("ufw deny out to 10.0.0.0/8")
os.system("ufw deny out to 172.16.0.0/12")
os.system("ufw deny out to 192.168.0.0/16")
os.system("ufw deny out to 100.64.0.0/10")
os.system("ufw deny out to 198.18.0.0/15")
os.system("ufw deny out to 169.254.0.0/1")
"""
#محدود کردن شل
time.sleep(4)
subprocess.run(["sudo", "groupadd", "restricted_shell"])
subprocess.run(["sudo", "sed", "-i", '$a/bin/rbash', "/etc/shells"])
os.system("clear")
os.system("ls /home")
time.sleep(5)
os.system("clear") 
os.system("ufw status")
time.sleep(5)
os.system("clear") 
print("End.....!")
os.system("sudo apt install screen -y")
os.system("screen python3 securityc.py ")