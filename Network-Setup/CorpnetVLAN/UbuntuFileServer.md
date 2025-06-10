# Ubuntu File Server Set Up

I installed Ubuntu Server on Virtualbox to use as a File Server mainly so the Windows 10 Machine can access any important files it needs to. I created the server with the creds itguy/admin

![Screenshot 2025-06-09 142514](https://github.com/user-attachments/assets/e3e0f4d5-2d5e-4bb2-8c0a-4d2cd9cef0ad)

After Ubuntu installed, I used a few packages to be able to share files across the network. Most notably, I ran `sudo apt install nfs-kernal-server`. This will allow us to share files to Windows using the NFS protocol. It's important to note here that for this to work you have to run `sudo apt update` and make sure the target Windows machine has either Windows 10 or Windows 11 **PRO** installed.

This took me a little while to figure out, but I had to run a head of commands to get this set up.

First, I created the shared folder in Ubuntu first by running

`sudo mkdir -p /mnt/sharedfolder`

`sudo chown nobody:nogroup /mnt/sharedfolder`

`sudo chmod 777 /mnt/sharedfolder`

Next, I had to edit the exports file in Ubuntu. This file determines what directories the server will export to using NFS.

`/mnt/sharedfolder  *(rw,sync,no_subtree_check)`

![Screenshot 2025-06-09 160349](https://github.com/user-attachments/assets/be9f2262-f700-4e66-84dc-5343178f16a6)

`sudo exportfs -a`

![Screenshot 2025-06-09 160404](https://github.com/user-attachments/assets/07bba4e9-3699-405d-992a-792a5a666644)

Lastly, I started and enabled the NFS server to run now and on every reboot.

`sudo systemctl enable nfs-server`

`sudo systemctl start nfs-server`


Ubuntu is all set and done! Now its time to move onto Windows which is something I had a particularly hard time with for a few reasons.

The first reason I had a hard time with Windows was because accessing the share was initally a pain, I would get thrown a few permission errors then have to reconfigure something or change a permission but I have the correct steps laid out below.


So, the first thing to do is type Win + R and type optionalfeatures. After this, I clicked to enable Services for NFS. The thing I missed here was I had to click on Services for NFS and the subdirectories for NFS to actually be enabled.

After this, it became simple. I went into command prompt as admin and ran mount -o anon \\192.168.1.104\mnt\sharedfolder Z:. This here specifies what directory we want to mount onto the system as well as the drive letter we assign it to. 


![Screenshot 2025-06-09 221038](https://github.com/user-attachments/assets/ebb966e4-0e1d-4877-a615-d05f26b1ea3b)

Thats it! The drive is finally mounted onto the machine and works.

![image](https://github.com/user-attachments/assets/2215c59c-93b1-4651-aaf9-95c14b98d65e)


## Setting Ubuntu IP addr

The last thing to do was very similar to what I had to do with the Splunk Server in the LognetVLAN folder, set a static IP. I set the static IP below using the netplan file.

![Screenshot 2025-06-09 222424](https://github.com/user-attachments/assets/43d84d48-d891-48b5-86b1-0defb1371295)

![Screenshot 2025-06-09 222306](https://github.com/user-attachments/assets/5f7d1607-4210-4f45-a37d-83f42bbdc236)
