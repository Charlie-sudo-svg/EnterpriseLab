# PFsense Installation

According to Netgate's website, PFsense is "The world’s leading open-source driven firewall, VPN, and services solution for network edge and cloud secure networking."

Downloading the ISO off the website, I opened Virtualbox to use the ISO to install PFsense. I made a VM with 256MB of ram and 2 processors. I also attached 4 network adapters to the VM, those being a NAT adapter, intnet called 'corpnet', intnet called 'scadanet', and an intnet called 'lognet.' These will be important later on as I set up VLANs.

When I start up the VM I go through the options until I reach
