from colorama import *
from bs4 import BeautifulSoup
import requests
import argparse
import os

# Require a "domain" argument from the user
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", required=True, help="Provide the name of the domain you want to search for.")
parser.add_argument("-o", "--output", required=False, help="Provide a name for the output file if you want to save the output.")
parser.add_argument("-g", "--grep", required=False, help="Grep the output to only return results that include a specified word.")
args = parser.parse_args()

# Append the user-specified domain to the url and make the request
url = f"https://crt.sh/?q={args.domain}"

# Check if filename provided exists before making the request
if os.path.isfile(args.output):
    print(Fore.RED + f"The file '{Fore.WHITE + args.output + Style.RESET_ALL + Fore.RED}' allready exists, quitting.")
    quit()
# Try the GET request, if there are any problems then display the except message
try:
    response = requests.get(url)
except:
    print(Fore.RED + f"Could not make a request to: {Fore.WHITE + url + Style.RESET_ALL}")
    quit()

# If the response code is 200 then proceed with grabbing all the common names and matching identities found in the search
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    common_name_elements = soup.select("table tr td:nth-of-type(5)")
    common_names = [element.text.strip() for element in common_name_elements]
    matching_identities_elements = soup.select("table tr td:nth-of-type(6)")
    matching_identities = [text.strip() for element in matching_identities_elements for text in element.stripped_strings]
    # Remove any duplicates from the lists above
    clean_cn_list = list(set(common_names))
    clean_mi_list = list(set(matching_identities))
    # If both output and grep arguments are used then do this
    if args.output and args.grep:
        with open(args.output, "x") as file:
            file.close()
        for site in clean_cn_list:
            if args.domain in site:
                with open(args.output, "a") as file:
                    file.write(site + "\n")
                    file.close()
                print(site)
        for site in clean_mi_list:
            if args.domain in clean_mi_list:
                with open(args.output, "a") as file:
                    file.write(site + "\n")
                    file.close()
                print(site)
    # If only the output argument is used then do this
    elif args.output:
        with open(args.output, "x") as file:
            file.close()
        for site in clean_cn_list:
            with open(args.output, "a") as file:
                file.write(site + "\n")
                file.close()
            print(site)
        for site in clean_mi_list:
            with open(args.output, "a") as file:
                file.write(site + "\n")
                file.close()
            print(site)
    # If only the grep argument is used then do this
    elif args.grep:
        for site in clean_cn_list:
            if args.domain in site:
                print(site)
        for site in clean_mi_list:
            if args.domain in site:
                print(site)
    # If neither the output or grep argument is used then do this
    else:
        for site in clean_cn_list:
            print(site)
        for site in clean_mi_list:
            print(site)
        quit()
# If there are any errors then display this message
else:
    print(Fore.RED + f"Could not make a request to: {Fore.WHITE + url + Style.RESET_ALL}")
    quit()
