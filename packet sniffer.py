from scapy.all import sniff, get_if_list


def packet_callback(packet):
    print(packet.summary())


def main():
    print("Available network interfaces:")
    for iface in get_if_list():
        print(iface)

    interface = input("Enter the network interface to sniff on (e.g., Ethernet, Wi-Fi): ")
    print(f"Sniffing on interface {interface}...")
    sniff(iface=interface, prn=packet_callback, store=False)


if __name__ == "__main__":
    main()
