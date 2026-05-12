import os
import socket

def ping(host):
    print("\n[+] Pinging target...\n")
    response = os.system(f"ping -c 1 {host}")

    if response == 0:
        print(f"{host} is Active")
    else:
        print(f"{host} is Inactive")

def port_check(host, port):
    print("\n[+] Checking port...\n")

    s = socket.socket()
    s.settimeout(2)

    result = s.connect_ex((host, port))

    if result == 0:
        print(f"Port {port} is OPEN on {host}")
    else:
        print(f"Port {port} is CLOSED on {host}")

    s.close()

def dns_lookup(domain):
    print("\n[+] Performing DNS Lookup...\n")

    try:
        ip = socket.gethostbyname(domain)
        print(f"IP Address of {domain}: {ip}")

    except:
        print("Invalid domain or unable to resolve")

while True:

    print("\n=== Cyber Network Detective ===")
    print("1. Ping Scanner")
    print("2. Port Checker")
    print("3. DNS Lookup")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        target = input("Enter IP/Domain: ")
        ping(target)

    elif choice == "2":
        target = input("Enter IP/Domain: ")
        port = int(input("Enter Port Number: "))
        port_check(target, port)

    elif choice == "3":
        domain = input("Enter Domain Name: ")
        dns_lookup(domain)

    elif choice == "4":
        print("Exiting tool...")
        break

    else:
        print("Invalid choice, try again")
