## About
A Python script aimed towards bug bounty hunters and penetration testers that outputs every result from a crt.sh search, removes any duplicate domain or subdomain from that result, and lets the user only output domains and subdomains that include a specific word, it also allows the user to save the results to a file to use in further enumeration
## Installation
```
git clone https://github.com/luddekn/crtsh-list
```
Install the script requirements:
```
pip3 install -r requirements.txt
```
## Usage
Output every result of the domain search:
```
python3 crtsh-list.py -d example.com
```
Save every result of the domain search to a specified file (file gets created for you):
```
python3 crtsh-list.py -d example.com -o results.txt
```
Grep the output to only include results that include the specific keyword:
```
python3 crtsh-list.py -d example.com -g example.com
```
Save the grepped output to a specified file (file gets created for you):
```
python3 crtsh-list.py -d example.com -g example.com -o results.txt
```


