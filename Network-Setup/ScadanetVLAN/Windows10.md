# Windows 10 SCADA Set Up

This set up will be a little bit different than an actual SCADA set up, primarily because there aren't any actual physical systems in place. 

To still make this as realisitic as possible, I will be coding a program in Python that will be launched from the Windows 10 machine that controls different "aspects" of
this company's water systems, including how many chemical are pumped into the water, the flow of water, etc.

## Water Application

I created a water application and packaged it into an `.exe` file for use. The code is listed in the ScadanetVLAN directory and is called water_control.py. It's supposed to be a very simple command line tool that allows the user to change the pH levels of the water with just a simple command. An example of the tool is shown below.

![image](https://github.com/user-attachments/assets/39862b81-e011-4016-becf-42235f846157)

The application also creates a log which shows everytime the pH level of water is changed as seen below.

![image](https://github.com/user-attachments/assets/e1348a07-8033-43c4-b6a3-df5c7c83894c)

Making the app was fairly simple as well as installing it. All I had to do was install vbox guest additions then mount the file onto the VM.

## Splunk Forwarder Installation

I installed Splunk Forwarder 9.4.3 and did a similar set up to the Windows 10 Client in the CorpnetVLAN. I launched the Forwarder and went through the options until I got to recieving host or indexer. Here, I put the IP of the Splunk Server which is 192.168.30.2.

![image](https://github.com/user-attachments/assets/b52a7197-40a3-44a7-a10b-83263fcb79cc)

After that I made the inputs.conf file and edited it as so 

![Screenshot 2025-06-11 134402](https://github.com/user-attachments/assets/ff206c37-0a5b-4219-bb79-87aebfca5162)

When I saved the inputs.conf file I went to Services in Windows and restarted the SplunkForwarder service. After this, I rebooted the machine for good measure then tested the application to make sure the logs were actually forwarding to the Splunk instance.

In my program I ran `main.exe --set-ph 5.4 --user Charlie`. It ran successfully. When I checked Splunk in the Telemetry index I saw the log got forwarded, perfect!

![image](https://github.com/user-attachments/assets/66da2247-6dd9-4371-b2f8-356c2c2614aa)


