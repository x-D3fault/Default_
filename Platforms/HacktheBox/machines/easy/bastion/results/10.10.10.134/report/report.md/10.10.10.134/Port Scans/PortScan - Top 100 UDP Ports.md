```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/xml/_top_100_udp_nmap.xml" 10.10.10.134
```

[/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/_top_100_udp_nmap.txt](file:///home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.92 scan initiated Sat May 21 13:35:27 2022 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/_top_100_udp_nmap.txt -oX /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/xml/_top_100_udp_nmap.xml 10.10.10.134
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
Increasing send delay for 10.10.10.134 from 0 to 50 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 10.10.10.134 from 50 to 100 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 10.10.10.134 from 100 to 200 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 10.10.10.134 from 200 to 400 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 10.10.10.134 from 400 to 800 due to 11 out of 12 dropped probes since last increase.
adjust_timeouts2: packet supposedly had rtt of -71147 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -71147 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -87451 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -87451 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -192991 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -192991 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -192454 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -192454 microseconds.  Ignoring time.
Nmap scan report for 10.10.10.134
Host is up, received user-set (0.040s latency).
Scanned at 2022-05-21 13:35:27 EDT for 275s
Not shown: 95 closed udp ports (port-unreach)
PORT     STATE         SERVICE     REASON      VERSION
123/udp  open|filtered ntp         no-response
138/udp  open|filtered netbios-dgm no-response
500/udp  open|filtered isakmp      no-response
4500/udp open|filtered nat-t-ike   no-response
5353/udp open|filtered zeroconf    no-response
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Microsoft Windows 2008|7
OS CPE: cpe:/o:microsoft:windows_server_2008:r2 cpe:/o:microsoft:windows_7
OS details: Microsoft Windows Server 2008 R2, Microsoft Windows 7
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=5/21%OT=%CT=%CU=7%PV=Y%DS=2%DC=T%G=N%TM=628923F2%P=x86
OS:_64-pc-linux-gnu)SEQ(CI=I%II=I)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=
OS:0%Q=)T6(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=80%W=0%S=
OS:Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=
OS:G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=80%CD=Z)

Network Distance: 2 hops

TRACEROUTE (using port 49194/udp)
HOP RTT      ADDRESS
1   36.61 ms 10.10.14.1
2   45.71 ms 10.10.10.134

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat May 21 13:40:02 2022 -- 1 IP address (1 host up) scanned in 274.94 seconds

```
