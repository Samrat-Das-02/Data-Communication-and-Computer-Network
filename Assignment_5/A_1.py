import ipaddress
from scapy.all import *

def send_icmp_ping(target_ip):
    # Craft an ICMP echo request packet
    icmp_request = IP(dst=target_ip)/ICMP()

    # Send the ICMP echo request and wait for a response
    reply = sr1(icmp_request, timeout=1, verbose=False)

    return reply

def main():
    try:
        network_address_str = input("Enter the network address (e.g., 192.168.1.0/24): ")
        network = ipaddress.IPv4Network(network_address_str, strict=False)

        # Iterate through all possible host IP addresses within the network
        for host_ip in network.hosts():
            host_ip_str = str(host_ip)
            reply = send_icmp_ping(host_ip_str)

            if reply:
                print(f"Host {host_ip_str} is online.")

    except ValueError:
        print("Invalid network address format.")
    except KeyboardInterrupt:
        print("\nScan aborted by user.")

if __name__ == "__main__":
    main()
