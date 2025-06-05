# Splunk Server Installation

I used Ubuntu 22.04.5 Server to set up the Splunk instance. The first thing I did was install the Ubuntu Server using the ISO file, I used the username itguy and the password admin to make things easy (for now.)

![Screenshot 2025-06-03 183222](https://github.com/user-attachments/assets/3251f5d4-1a79-4e6f-97fd-bb7601aa8a39)

After installing Ubuntu I had to do a few things before I got started installing Splunk. I first changed the file /etc/netplan/50-cloud-init.yaml to the configured one pictured below, this set a static IP address of 192.168.30.2 and used 2 nameservers 8.8.8.8 and 1.1.1.1.

![Screenshot 2025-06-03 184224](https://github.com/user-attachments/assets/7218a3be-d2bb-4216-b31e-22c2406e88aa)

I also made sure to configure the file /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg with `network: {network: disabled}` inside of it so the static IP persists on reboot. 

After that, I ran into some issues accessing the internet. This prompted me to troubleshoot network issues for an hour before realizing that the WAN interface in Pfsense is configured with a static IP and it must be configured with DHCP for routing to work. I also needed to add an allow rule to the WAN interface that allowed traffic from the internet. 

Configuring the shared folder was easy, I downloaded Splunk 9.4.2 onto my host laptop and created a folder called SplunkServer. I then created a shared folder in VirtualBox which I was able to mount to /mnt, and after running these commands below and rebooting, I was able to access the shared folder.

`sudo apt install build-essential dkms linux-headers-$(uname -r)`

`sudo mount /dev/cdrom /mnt`

`sudo /mnt/VBoxLinuxAdditions.run`

`sudo usermod -aG vboxsf itguy`

Once the shared folder was accessed, I ran `sudo dpkg -i splunk-9.4.2-e9664af3d956-linux-amd64.deb` and waited a few minutes for the file to unpack.

From here, the file will be accessed through /opt/splunk where the rest of the setup will occur.

I went to /opt/splunk/bin and ran the command `sudo ./splunk start --accept-license`. This started the Splunk server and I also ran `sudo ./splunk enable boot-start` to have the splunk server start everytime the Ubuntu server is booted online. 

Now to check if the Splunk is online and working I go to 192.168.30.2:8000 in my browser and I login using the creds I provided at startup which are itguy/administrator and it works!

![image](https://github.com/user-attachments/assets/f1dd4639-ef85-49bd-926e-36b822f1fe86)

Now that Splunk is online, I can start to set up other machines and use Sysmon and the Splunk forwarder to help forward log telemetry to Splunk to analyze.
