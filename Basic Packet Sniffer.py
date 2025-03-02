import scapy.all as scapy
import argparse

def packet_callback(packet):
    print(packet.summary())

def sniff_packets(interface, count):
    print(f"Sniffing on {interface}... Press Ctrl+C to stop.")
    scapy.sniff(iface=interface, count=count, prn=packet_callback, store=False)

def main():
    parser = argparse.ArgumentParser(description="Packet Sniffer using Scapy")
    parser.add_argument("interface", help="Network interface to sniff on (e.g., eth0, wlan0)")
    parser.add_argument("-c", "--count", type=int, default=0, help="Number of packets to capture (0 for unlimited)")
    
    args = parser.parse_args()
    sniff_packets(args.interface, args.count)

if __name__ == "__main__":
    main()
