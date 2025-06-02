# PFsense Installation

According to Netgate's website, PFsense is "The world’s leading open-source driven firewall, VPN, and services solution for network edge and cloud secure networking."

Downloading the ISO off the website, I opened Virtualbox to use the ISO to install PFsense. I made a VM with 256MB of ram and 2 processors. I also attached 4 network adapters to the VM, those being a NAT adapter, intnet called 'corpnet', intnet called 'scadanet', and an intnet called 'lognet.' These will be important later on as I set up VLANs.

When I start up the VM I go through the options and add bridged adapter as the WAN interface and the corpnet adapter as the LAN interface. When PFsense is done installing, I get rid of the ISO from the boot order and PFsense is successfully installed!

I was able to access it from another computer on the corporate LAN network.

![Screenshot 2025-06-01 194752](https://github.com/user-attachments/assets/376afe1c-35c2-4ba4-b71e-36f2936ecd48)


## Adding Interfaces

The next step was to add OPT1 and OPT2 as interfaces in PFsense to segment the networks. I first added OPT1 as an interface on the IP 192.168.50.1/24 this will be our SCADA subnet. 

![image](https://github.com/user-attachments/assets/a6dc2fc7-949c-40ce-b920-3401badbd1e2)

After I added OPT1 as an interface, I went to Firewall -> Rules and added a rule that allows any type of traffic (TCP, UDP, ICMP) through to the IP. This is important for right now so that any computer on SCADA net can actually ping the default gateway.

![image](https://github.com/user-attachments/assets/47c2b5cb-2cef-41d7-9bca-e08fa5056924)

I followed the same ideas for OPT2 too. I created the interface and used the IP 192.168.30.1/24, this will be our logging subnet where the Splunk server will be hosted.

![image](https://github.com/user-attachments/assets/a208923c-eca7-40ec-b72d-c6c145b6d85d)

Enabling the DHCP server for both interfaces is also crucial as well, this was done in the PFsense server.

![Screenshot 2025-06-02 160234](https://github.com/user-attachments/assets/6b084298-84a0-4bde-b5db-a643f16f2cca)


