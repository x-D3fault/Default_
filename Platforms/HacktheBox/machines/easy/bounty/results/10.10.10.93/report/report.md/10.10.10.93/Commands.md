```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/xml/_quick_tcp_nmap.xml" 10.10.10.93

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/_full_tcp_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/xml/_full_tcp_nmap.xml" 10.10.10.93

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/xml/_top_100_udp_nmap.xml" 10.10.10.93

feroxbuster -u http://10.10.10.93:80/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"

curl -sSik http://10.10.10.93:80/

curl -sSikf http://10.10.10.93:80/.well-known/security.txt

curl -sSikf http://10.10.10.93:80/robots.txt

nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/tcp80/xml/tcp_80_http_nmap.xml" 10.10.10.93

whatweb --color=never --no-errors -a 3 -v http://10.10.10.93:80 2>&1

wkhtmltoimage --format png http://10.10.10.93:80/ /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/tcp80/tcp_80_http_screenshot.png


```