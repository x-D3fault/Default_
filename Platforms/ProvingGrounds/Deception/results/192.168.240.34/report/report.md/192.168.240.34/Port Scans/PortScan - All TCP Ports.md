```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/_full_tcp_nmap.txt" -oX "/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/xml/_full_tcp_nmap.xml" 192.168.240.34
```

[/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/_full_tcp_nmap.txt](file:///home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/_full_tcp_nmap.txt):

```
# Nmap 7.92 scan initiated Sun Apr 10 00:03:03 2022 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/_full_tcp_nmap.txt -oX /home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/xml/_full_tcp_nmap.xml 192.168.240.34
Nmap scan report for 192.168.240.34
Host is up, received user-set (0.047s latency).
Scanned at 2022-04-10 00:03:03 EDT for 66s
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 9d:d0:98:da:0d:32:3d:0b:3f:42:4d:d7:93:4f:fd:60 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDLSsGJtpg5KvawG56yanORlHOGP7anzFKXq8ZDjuBD20sWrHl6g0J1+w497SyvRnB6EDOBGrjqlEXqlI7DvgrAo08GOCvoajuPpitLuC2rCfRC3b3ctn/n2+zGkkfsD5Y0U6PQrchRNpMKH/4nsaBcrTV8ZkEGF+VNYhnTO7c1vGhpH0i5c7UzyKvfqz/KzH4YryUpC1opxB9pn0jHH+iQ8H+Brne/bvOmpyvoy84CzuunshxMmAV9qdaLmZxOOF25SF5uHh6r1h8tVG8yLbD1N7IfPXXy0GpZZZIBt4i/ZQVpfk1i0GsY4/mL3VCrtFsO4p2PxRLVws5Fpces+pDN
|   256 4c:f4:2e:24:82:cf:9c:8d:e2:0c:52:4b:2e:a5:12:d9 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDwKM2aO1LW/C4gfLHyFmkrfcPcXVHvIEK8JN9pk/9kNhZKz8X9byyxiWMnNS/6AQNMAV0d5B+d0/VK2eps90ZI=
|   256 a9:fb:e3:f4:ba:d6:1e:72:e7:97:25:82:87:6e:ea:01 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEOULyvRe2blVRaHM9twRKyE34SQUyGPMjVmRv2srgvv
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: POST OPTIONS HEAD GET
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.29 (Ubuntu)
Aggressive OS guesses: Linux 2.6.32 (91%), Linux 2.6.32 or 3.10 (91%), Linux 3.5 (91%), WatchGuard Fireware 11.8 (91%), Synology DiskStation Manager 5.1 (90%), Linux 2.6.35 (90%), Linux 2.6.39 (90%), Linux 3.10 - 3.12 (90%), Linux 4.2 (90%), Linux 4.4 (90%)

```
