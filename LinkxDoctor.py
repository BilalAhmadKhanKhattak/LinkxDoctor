import requests  # For Making HTTP requests to a webpage
from bs4 import BeautifulSoup  # BeautifulSoup is used for parsing the HTML content and extracting Data
from urllib.parse import urljoin, urlparse  # For handling and manipulating URLs
from colorama import Fore, init  # Obviously, Program Needs Some COLORS too ;)
import time  # For Handling Delays

# Initialize Colorama
init(autoreset=True)

banner = ("\n"
          " _     _       _          ____             _             \n"
          "| |   (_)_ __ | | ____  _|  _ \  ___   ___| |_ ___  _ __ \n"
          "| |   | | '_ \| |/ /\ \/ / | | |/ _ \ / __| __/ _ \| '__|\n"
          "| |___| | | | |   <  >  <| |_| | (_) | (__| || (_) | |   \n"
          "|_____|_|_| |_|_|\_\/_/\_\____/ \___/ \___|\__\___/|_|    V 1.1\n"
          
          "                                                                By Mr Bilred\n"
          "Github: https://github.com/BilalAhmadKhanKhattak\n"
          "Bilal Ahmad Khan AKA Bilred..."
          "\n------------------------------------------------------------------------"
          "\n"
          "LinkxDoctor is an advanced, Python-based tool designed to help web developers,\n"
          "SEO specialists, bug hunters, Ethical Hackers and website admins maintain the integrity of their websites.\n"
          "By scanning any given webpage, LinkxDoctor identifies both broken and valid links,\n"
          "ensuring that all the hyperlinks on the page are functioning correctly \n"
          "a report on the link status, helping ensure all links on the page are functional.\n"
          "This Project Is Indeed The Successor Of One Of My Previous Projects, LinkxDoxer\n")
print(Fore.CYAN + banner)


def get_all_links(url, retries=5, delay=1):
    """
    Extracts All The Links From The Given Webpage
    """
    for attempt in range(retries):
        try:
            response = requests.get(url)
            if response.status_code != 200:
                print(Fore.RED + f"Failed to retrieve webpage, STATUS CODE = {response.status_code}")
                return []

            soup = BeautifulSoup(response.content, features='html.parser')
            links = [urljoin(url, a['href']) for a in soup.find_all(name='a', href=True)]
            return links

        except requests.exceptions.MissingSchema:
            print(Fore.YELLOW + "Invalid URL Format. Please Include http:// or https://")
            return []
        except requests.exceptions.RequestException as e:
            print(Fore.YELLOW + f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
        except Exception as e:
            print(Fore.RED + f"An Unknown Error Occurred: {e}")
            return []
    print(Fore.RED + "Max Retries Exceeded")
    return []


def is_broken_link(url, retries=3, delay=1):
    """
    Check if the given URL is broken
    """
    for attempt in range(retries):
        try:
            response = requests.head(url, allow_redirects=True)
            if response.status_code in {404, 500}:
                return True
            return False
        except requests.exceptions.RequestException:
            time.sleep(delay)
    return True


def check_broken_links(url):
    """
    Checks all links on the given webpage and identifies broken links
    """
    links = get_all_links(url)
    if not links:
        print(Fore.RED + "No links found or an error occurred")
        return [], []

    broken_links = []
    valid_links = []

    for i, link in enumerate(links, start=1):
        if is_broken_link(link):
            broken_links.append(link)
            print(Fore.RED + f"{i}. Broken Link: {link}")
        else:
            valid_links.append(link)
            print(Fore.GREEN + f"{i}. Valid Link: {link}")

    return broken_links, valid_links


def save_links_to_file(broken_links, valid_links):  # Function for the save to file logic
    save_to_file = input("Do you want to save the links to a file? (y/n): ").strip().lower()
    if save_to_file == 'y':
        filename = input("Enter the filename (default: links_report.txt THIS CAN OVERWRITE THE PREVIOUS ONE TOO, "
                         "IF EXISTED): ").strip()
        if not filename:
            filename = "links_report.txt"

        try:
            with open(filename, 'w') as file:
                if valid_links:
                    file.write("Valid Links:\n")
                    for link in valid_links:
                        file.write(link + '\n')

                if broken_links:
                    file.write("\nBroken Links:\n")
                    for link in broken_links:
                        file.write(link + '\n')

            print(Fore.GREEN + f"Links have been saved to {filename}")
        except Exception as e:
            print(Fore.RED + f"Failed to save the file: {e}")
    else:
        print(Fore.YELLOW + "Links were not saved to a file.")


if __name__ == "__main__":
    website_url = input("Enter the Website URL (include https:// or http://): ")
    parsed_url = urlparse(website_url)
    if not parsed_url.scheme:  # this block is run if URL is missing schema, e.g., https:// or http://
        website_url = 'https://' + website_url

    broken_links, valid_links = check_broken_links(website_url)

    if broken_links:
        print(Fore.RED + f"\nFound {len(broken_links)} broken links.")
    else:
        print(Fore.GREEN + "No Broken Hearted Links Found")

    save_links_to_file(broken_links, valid_links)
    print("Press any key to exit...")
    input()
