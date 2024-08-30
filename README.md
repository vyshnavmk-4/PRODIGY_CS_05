# PRODIGY_CS_05
Description
This script uses the Scapy library to sniff network packets on a specified interface and analyze their details. It captures packets and displays information such as source and destination IP addresses, protocol types (TCP, UDP, ICMP), source and destination ports, and payload data. This tool is useful for network analysis and debugging.
Features
1.IP Layer Analysis: Displays source and destination IP addresses.
2.Protocol Detection: Identifies and reports on TCP, UDP, and ICMP protocols.
3.Port Information: Shows source and destination ports for TCP and UDP packets.
4.Payload Display: Prints payload data if present in the packet.

Installation
Ensure scapy is installed. You can install it using pip:
python your_script_name.py

Usage
Run the Script: Execute the script from the command line
python your_script_name.py
Enter Network Interface: When prompted, enter the network interface you want to sniff on (e.g., eth0, wlan0).
View Output: The script will start capturing packets and display the information in the console.


Important
Permissions: Running packet sniffing tools may require administrative or root permissions. Make sure you have the necessary rights to capture network traffic on your system.
Ethical Use: Use this tool responsibly and only on networks where you have explicit permission to capture and analyze traffic.
