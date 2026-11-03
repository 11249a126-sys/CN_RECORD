Aim:
To simulate Address Resolution Protocol (ARP) and Reverse Address Resolution Protocol (RARP) for mapping IP addresses to MAC addresses and MAC addresses to IP addresses.
Algorithm:
58.	Begin the program and define the ARP and RARP tables.
59.	Store IP-to-MAC address mappings in the ARP table.
60.	Create the reverse MAC-to-IP mappings for the RARP table.
61.	For an ARP request, accept an IP address and search the ARP table.
62.	Display the corresponding MAC address if the IP address is present; otherwise display that it is not found.
63.	For a RARP request, accept a MAC address and search the RARP table.
64.	Display the corresponding IP address if the MAC address is present; otherwise display that it is not found.
65.	Display both address tables.
66.	Add a new IP and MAC address entry and update both tables.
67.	Display the updated tables and stop the program.
Program:

class ARP_RARP_Simulator:
 
    def __init__(self):
 
        # ARP Table: IP Address -> MAC Address
        self.arp_table = {
            "192.168.1.1": "00:0a:95:9d:68:16",
            "192.168.1.2": "00:0a:95:9d:68:17",
            "192.168.1.3": "00:0a:95:9d:68:18"
        }
 
        # RARP Table: MAC Address -> IP Address
        self.rarp_table = {
            mac: ip
            for ip, mac in self.arp_table.items()
        }
 
    # ARP: IP Address -> MAC Address
    def arp_request(self, ip_address):
        print("\n----------------------------------------")
        print("ARP REQUEST")
        print("----------------------------------------")
 
        print(
            f"ARP Request: Who has {ip_address}? "
            "Tell me your MAC address."
        )
 
        # Search for IP address
        mac_address = self.arp_table.get(ip_address)
 
        if mac_address:
 
            print(
                f"ARP Reply: {ip_address} "
                f"is at {mac_address}."
            )
 
            return mac_address
 
        else:
 
            print(
                f"ARP Reply: {ip_address} "
                "is not found."
            )
 
            return None
 
    # RARP: MAC Address -> IP Address
    def rarp_request(self, mac_address):
 
        print("\n----------------------------------------")
        print("RARP REQUEST")
        print("----------------------------------------")
 
        print(
            f"RARP Request: Who has MAC address "
            f"{mac_address}? Tell me your IP address."
        )
 
        # Search for MAC address
        ip_address = self.rarp_table.get(mac_address)
 
        if ip_address:
 
            print(
                f"RARP Reply: {mac_address} "
                f"is associated with IP {ip_address}."
            )
 
            return ip_address
 
        else:
 
            print(
                f"RARP Reply: {mac_address} "
                "is not found."
            )
 
            return None
 
    # Display ARP Table
    def display_arp_table(self):
 
        print("\n========================================")
        print("ARP TABLE")
        print("========================================")
 
        print("IP Address\t\tMAC Address")
        print("----------------------------------------")
 
        for ip, mac in self.arp_table.items():
 
            print(f"{ip}\t\t{mac}")
 
    # Display RARP Table
    def display_rarp_table(self):
 
        print("\n========================================")
        print("RARP TABLE")
        print("========================================")
 
        print("MAC Address\t\t\tIP Address")
        print("----------------------------------------")
 
        for mac, ip in self.rarp_table.items():
 
            print(f"{mac}\t{ip}")
 
    # Add new IP and MAC entry
    def add_entry(self, ip_address, mac_address):
 
        self.arp_table[ip_address] = mac_address
        self.rarp_table[mac_address] = ip_address
 
        print("\nEntry added successfully.")
 
        print(f"IP  : {ip_address}")
        print(f"MAC : {mac_address}")
 
 
# Main Program
if __name__ == "__main__":
 
    # Create simulator
    simulator = ARP_RARP_Simulator()
 
    print("\n==============================================")
    print("          ARP AND RARP SIMULATOR")
    print("==============================================")
 
    # Display ARP table
    simulator.display_arp_table()
 
    # Display RARP table
    simulator.display_rarp_table()
 
    # ARP Examples
    print("\n========== ARP EXAMPLES ==========")
 
    simulator.arp_request("192.168.1.1")
 
    simulator.arp_request("192.168.1.2")
 
    simulator.arp_request("192.168.1.100")
 
    # RARP Examples
    print("\n========== RARP EXAMPLES ==========")
 
    simulator.rarp_request(
        "00:0a:95:9d:68:16"
    )
 
    simulator.rarp_request(
        "00:0a:95:9d:68:17"
    )
 
    simulator.rarp_request(
        "00:0a:95:9d:68:99"
    )
 
    # Add new entry
    print("\n========== ADD NEW ENTRY ==========")
 
    simulator.add_entry(
        "192.168.1.4",
        "00:0a:95:9d:68:19"
    )
 
    # Display updated tables
    simulator.display_arp_table()
 
    simulator.display_rarp_table()
