# Network-Scanner

The tool is used to determine live host on the network using Scapy.

## ARP:

ARP stands for Address Resolution Protocol. When you try to ping an IP address on your local network, say 192.168.1.1, your system has to turn the IP address 192.168.1.1 into a MAC address. This involves using ARP to resolve the address, hence its name.

Systems keep an ARP look-up table where they store information about what IP addresses are associated with what MAC addresses. When trying to send a packet to an IP address, the system will first consult this table to see if it already knows the MAC address. If there is a value cached, ARP is not used.

If the IP address is not found in the ARP table, the system will then send a broadcast packet to the network using the ARP protocol to ask "who has 192.168.1.1". Because it is a broadcast packet, it is sent to a special MAC address that causes all machines on the network to receive it. Any machine with the requested IP address will reply with an ARP packet that says "I am 192.168.1.1", and this includes the MAC address which can receive packets for that IP.

### ARP Scan:
1) Consider a device wants to find out live host on the network then first it will send a broadcast to all machines.
2) Then machines which are up, reply with their Mac Address to attacker
3) This scan is performed on the complete subnet.

## Usage:

python networkscanner_new.py -t IP/Subnet

### Requirements:
1)optarse
2)scapy

#### Download Requirements:

pip install -r requirements.txt

#### Download:

1) git clone https://github.com/devansh3008/Network-Scanner.git 
2) cd Network-Scanner
3) python networkscanner_new.py -t 192.168.43.1/24


