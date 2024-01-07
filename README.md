## About
This script takes every domain from a https://crt.sh/ search and removes any duplicates, it also lets the user grep and save the output. You can then use this list in further enumeration to see what domains and subdomains are alive or not.
## Installation
```
git clone https://github.com/luddekn/crtsh-list
```
Install the script requirements:
```
pip install -r requirements.txt
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


