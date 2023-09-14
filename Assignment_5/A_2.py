from scapy.all import *

def send_syn_scan(target_ip, port_range):
    open_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        # Craft a TCP SYN packet
        packet = IP(dst=target_ip) / TCP(sport=RandShort(), dport=port, flags="S")

        # Send the TCP SYN packet and wait for a response
        response = sr1(packet, timeout=1, verbose=False)

        if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            # If the response is a TCP SYN+ACK packet, the port is open
            open_ports.append(port)

    return open_ports

def main():
    try:
        target_ip = input("Enter the host IP address: ")
        port_range = (0, 1023)  # Port range to scan (0 to 1023)

        open_ports = send_syn_scan(target_ip, port_range)

        if open_ports:
            print("Open ports on the target host:")
            for port in open_ports:
                print(f"Port {port} is open.")
        else:
            print("No open ports found on the target host.")

    except KeyboardInterrupt:
        print("\nScan aborted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
