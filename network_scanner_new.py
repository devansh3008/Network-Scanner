#!/usr/bin/env python
import scapy.all as scapy
import optparse

def argument():
 parserobj=optparse.OptionParser() 
 parserobj.add_option("-r","--target",dest="target",help="Enter Range to Scan:")
 options, arguments=parserobj.parse_args()
 return options

def scan(ip):
 arp_request=scapy.ARP(pdst=ip)
 broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff:") 
 arp_packet=broadcast/arp_request
 answered, uanswered=scapy.srp(arp_packet,timeout=1,verbose=0)
 ip_list=[]
 for element in answered:
  final_list={"ip":element[1].psrc,"mac":element[1].hwsrc}
  ip_list.append(final_list)
  return ip_list

def display(results):
 print("IP\t\t\tMAC\n---------------------------------")
 for values in results:
  print(values['ip'] + "\t\t" + values['mac'])

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)


