# Windows 10 SCADA Set Up

This set up will be a little bit different than an actual SCADA set up, primarily because there aren't any actual physical systems in place. 

To still make this as realisitic as possible, I will be coding a program in Python that will be launched from the Windows 10 machine that controls different "aspects" of
this company's water systems, including how many chemical are pumped into the water, the flow of water, etc.

## Splunk Forwarder Installation

I installed Splunk Forwarder 9.4.3 and did a similar set up to the Windows 10 Client in the CorpnetVLAN. I launched the Forwarder and went through the options until I got to recieving host or indexer. Here, I put the IP of the Splunk Server which is 192.168.30.2.
