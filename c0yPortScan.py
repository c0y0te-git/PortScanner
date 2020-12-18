
# Port Scanner

import socket
import termcolor

def scan(target, ports):
    print("\n" + "[!]Starting Scan For " + str(target))
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(termcolor.colored((f"[+] Port {port} is OPEN!"), "green"))
        sock.close()
    except:
        #print(f"[-] Port {port} is CLOSED!")
        pass


# Start of Program
print(termcolor.colored(("[!] Welcome to c0y0te's Port Scanner! [!]"), "red"))
targets = input("[*] Enter Target IP's to Scan (ex. 192.168.1.1, 192.168.2.2): ")
ports = int(input("[*] Enter Max Ports to Scan (ex. 500): ")) + 1
if "," in targets:
    print(termcolor.colored(("[*] Scanning Multiple Targets..."), "blue"))
    for ip_addr in targets.split(","):
        scan(ip_addr.strip(" "), ports)
else:
    scan(targets, ports)