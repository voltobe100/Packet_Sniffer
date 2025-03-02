# Packet Sniffer

A simple packet sniffer built using Python and Scapy to capture and analyze network packets.

## Features

- Captures packets on a specified network interface
- Displays packet summaries in real-time
- Allows limiting the number of packets to capture

## Requirements

- Python 3
- Scapy library

## Installation

```bash
pip install scapy
```

## Usage

```bash
python packet_sniffer.py <interface> [-c COUNT]
```

### Examples

- Capture packets on `eth0`:
  ```bash
  python packet_sniffer.py eth0
  ```
- Capture 10 packets on `wlan0`:
  ```bash
  python packet_sniffer.py wlan0 -c 10
  ```

## Notes

- Run the script with administrator privileges (e.g., using `sudo` on Linux).
- Ensure the network interface is active.
