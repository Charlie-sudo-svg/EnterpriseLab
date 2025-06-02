# PFsense Installation

According to Netgate's website, PFsense is "The world’s leading open-source driven firewall, VPN, and services solution for network edge and cloud secure networking."

Downloading the ISO off the website, I opened Virtualbox to use the ISO to install PFsense. I made a VM with 256MB of ram and 2 processors. I also attached 4 network adapters to the VM, those being a NAT adapter, intnet called 'corpnet', intnet called 'scadanet', and an intnet called 'lognet.' These will be important later on as I set up VLANs.

When I start up the VM I go through the options and add bridged adapter as the WAN interface and the corpnet adapter as the LAN interface. When PFsense is done installing, I get rid of the ISO from the boot order and PFsense is successfully installed!

I was able to access it from another computer on the corporate LAN network.

![Screenshot 2025-06-01 194752](https://github.com/user-attachments/assets/376afe1c-35c2-4ba4-b71e-36f2936ecd48)


## Adding Interfaces

The next step was to add OPT1 and OPT2 as interfaces in PFsense to segment the networks. I first added OPT1 as an interface on the IP 192.168.50.1/24 this will be our SCADA subnet. 

*show screenshot of opt1
