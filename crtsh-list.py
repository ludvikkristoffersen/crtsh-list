from colorama import *
from bs4 import BeautifulSoup
import requests
import argparse
import os

# Require a "domain" argument from the user
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", required=True, help="Provide the name of the domain you want to search for.")
parser.add_argument("-o", "--output", required=False, help="Provide a name for the output file if you want to save the output.")
parser.add_argument("-g", "--grep", required=False, help="Grep the output to only return results that include the name of the domain.")
parser.add_argument("-fs", "--filters", required=False, help="Filter out specific words from the output, such as www. or *. for example, you can filter multiple words using a comma (example: -fs *.,www).")
args = parser.parse_args()

# Append the user-specified domain to the url and make the request
url = f"https://crt.sh/?q={args.domain}"

# Check if filename provided exists before making the request
if args.output:
    if os.path.isfile(args.output):
        print(Fore.RED + f"The file '{Fore.WHITE + args.output + Style.RESET_ALL + Fore.RED}' allready exists, quitting.")
        quit()
# Try the GET request, if there are any problems then display the except message
try:
    response = requests.get(url)
except:
    print(Fore.RED + f"Could not make a request to: {Fore.WHITE + url + Style.RESET_ALL}")
    quit()

# Defining some functions
def output_grep_filter():
    filters_list = args.filters.split(",")
    filters_list = [filter.strip() for filter in filters_list]
    with open(args.output, "x") as file:
        file.close()
    for site in result_list:
        if all(filter not in site for filter in filters_list):
            if args.grep in site:
                with open(args.output, "a") as file:
                    file.write(site + "\n")
                    file.close()
                print(site)
def output_grep():
    with open(args.output, "x") as file:
        file.close()
    for site in result_list:
        if args.grep in site:
            with open(args.output, "a") as file:
                file.write(site + "\n")
                file.close()
            print(site)
def output_filter():
    filters_list = args.filters.split(",")
    filters_list = [filter.strip() for filter in filters_list]
    with open(args.output, "x") as file:
        file.close()
    for site in result_list:
        if all(filter not in site for filter in filters_list):
            with open(args.output, "a") as file:
                file.write(site + "\n")
                file.close()
            print(site)
def grep_filter():
    filters_list = args.filters.split(",")
    filters_list = [filter.strip() for filter in filters_list]
    for site in result_list:
        if all(filter not in site for filter in filters_list):
            if args.grep in site:
                print(site)
def output():
    with open(args.output, "x") as file:
        file.close()
    for site in result_list:
        with open(args.output, "a") as file:
            file.write(site + "\n")
            file.close()
        print(site)
def grep():
    for site in result_list:
        if args.grep in site:
            print(site)
def filter():
    filters_list = args.filters.split(",")
    filters_list = [filter.strip() for filter in filters_list]
    for site in result_list:
        if all(filter not in site for filter in filters_list):
            print(site)

# If the response code is 200 then proceed with grabbing all the common names and matching identities found in the search
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    common_name_elements = soup.select("table tr td:nth-of-type(5)")
    common_names = [element.text.strip() for element in common_name_elements]
    matching_identities_elements = soup.select("table tr td:nth-of-type(6)")
    matching_identities = [text.strip() for element in matching_identities_elements for text in element.stripped_strings]
    # Remove any duplicates from the lists above
    combined_list = common_names + matching_identities
    result_list = set(combined_list)
    # If every argument is used then do this
    if args.output and args.grep and args.filters:
        output_grep_filter()
    # If only output and grep argument is used then do this
    elif args.output and args.grep:
        output_grep()
    # If only output and filter argument is used then do this
    elif args.output and args.filters:
        output_filter()
    # If only grep and filter argument is used then do this
    elif args.grep and args.filters:
        grep_filter()
    # If only the output argument is used then do this
    elif args.output:
        output()
    # If only the grep argument is used then do this
    elif args.grep:
        grep()
    # If only the filter argument is used then do this
    elif args.filters:
        filter()
    # If no filters are used then do this
    else:
        for site in result_list:
            print(site)
# If there are any errors then display this message
else:
    print(Fore.RED + f"Could not make a request to: {Fore.WHITE + url + Style.RESET_ALL}")
    quit()
