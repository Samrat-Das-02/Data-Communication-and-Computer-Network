from scapy.all import *

# Step 1: Capture 10000 packets (offline)
packets = sniff(count=100)

# Uncomment the following line if you want to capture packets online (live capture)
# packets = sniff(count=10000)

# Step 3: Count TCP/UDP segments and calculate average payload length
quadruples = {}  # Dictionary to store quadruples as keys and their data as values

for packet in packets:
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        else:
            continue  # Skip other protocols

        quadruple = (src_ip, dst_ip, src_port, dst_port, protocol)

        if quadruple not in quadruples:
            quadruples[quadruple] = {"segments": 0, "payload_length": 0}

        quadruples[quadruple]["segments"] += 1
        quadruples[quadruple]["payload_length"] += len(packet)

print("Source IP\tDestination IP\tProtocol\tSource Port\tDestination Port\tSegments\tAverage Payload Length")
for quadruple, data in quadruples.items():
    src_ip, dst_ip, src_port, dst_port, protocol = quadruple
    segments = data["segments"]
    avg_payload_length = data["payload_length"] / segments if segments > 0 else 0
    print(f"{src_ip}\t{dst_ip}\t{protocol}\t{src_port}\t{dst_port}\t{segments}\t{avg_payload_length:.2f}")