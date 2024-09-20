from scapy.all import *

def packet_handler(packet):
    if packet.haslayer(Dot11Beacon):
        ssid = packet[Dot11Elt].info.decode()
        bssid = packet[Dot11].addr2
        print(f"SSID: {ssid}, BSSID: {bssid}")

sniff(iface="wlan0", prn=packet_handler, count=10)
