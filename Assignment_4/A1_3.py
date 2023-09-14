from scapy.all import *

packets = sniff(count=5) #online

host_ips = set() #unique host addresses
for packet in packets:
    if IP in packet:
        host_ips.add(packet[IP].src)
        host_ips.add(packet[IP].dst)

print("Distinct host IP addresses:")
for ip in host_ips:
    print(ip)

segment_counts = {} #segment count
payload_lengths = {} #payload length
# ( src, dst, protocol)
for packet in packets:
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        else:
            continue  # Skip other protocols

        if (src_ip, dst_ip, protocol) not in segment_counts:
            segment_counts[(src_ip, dst_ip, protocol)] = 0
            payload_lengths[(src_ip, dst_ip, protocol)] = 0

        segment_counts[(src_ip, dst_ip, protocol)] += 1
        payload_lengths[(src_ip, dst_ip, protocol)] += len(packet)

print("\nSegment counts and average payload lengths:")
for key, count in segment_counts.items():
    src_ip, dst_ip, protocol = key #(src, dst, proto)
    avg_payload_length = payload_lengths[key] / count
    print(f"Src: {src_ip}, Dst: {dst_ip}, Protocol: {protocol}, "
          f"Segments: {count}, Avg Payload Length: {avg_payload_length:.2f}")