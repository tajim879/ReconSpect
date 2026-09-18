import os
import sys
import time
import socket
import requests
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"""{Fore.CYAN}
  ██████╗ ███████╗ ██████╗ ██████╗ ███████╗██████╗ ███████╗ ██████╗████████╗
  ██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝
  ██████╔╝█████╗  ██║     ██║   ██║███████╗██████╔╝█████╗  ██║        ██║   
  ██╔══██╗██╔══╝  ██║     ██║   ██║╚════██║██╔═══╝ ██╔══╝  ██║        ██║   
  ██║  ██║███████╗╚██████╗╚██████╔╝███████║██║     ███████╗╚██████╗   ██║   
  ╚═╝  ╚═╝╚══════╝ ╚══════╝ ╚══════╝╚══════╝╚═╝     ╚══════╝ ╚══════╝   ╚═╝   
    {Style.DIM}{Fore.GREEN}                  [ v1.0 - Automated Recon & OSINT Tool ]
                      [ Coded by: Tajim Uddin ]{Style.RESET_ALL}
""")

def main_menu():
    clear_screen()
    banner()
    print(f"{Fore.YELLOW}  [::] Choose Recon Type / Module [::]{Style.RESET_ALL}\n")
    print(f"    {Fore.GREEN}[01]{Fore.RESET} Full Recon (IP & Basic DNS Scan)")
    print(f"    {Fore.GREEN}[02]{Fore.RESET} IP Geolocation Lookup")
    print(f"    {Fore.GREEN}[03]{Fore.RESET} DNS Records Check")
    print(f"    {Fore.GREEN}[99]{Fore.RESET} About Tool")
    print(f"    {Fore.RED}[00]{Fore.RESET} Exit\n")
    
    choice = input(f"{Fore.CYAN}  recon@spect:~# {Style.RESET_ALL}")
    return choice

def ip_lookup():
    clear_screen()
    banner()
    domain = input(f"{Fore.YELLOW}[?] Enter Domain or IP (e.g., example.com): {Style.RESET_ALL}")
    if not domain:
        return
    
    print(f"\n{Fore.BLUE}[*] Resolving IP address...{Style.RESET_ALL}")
    try:
        ip = socket.gethostbyname(domain)
        print(f"{Fore.GREEN}[+] Target IP: {ip}{Style.RESET_ALL}")
        
        print(f"{Fore.BLUE}[*] Fetching Geolocation details...{Style.RESET_ALL}")
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        
        if data['status'] == 'success':
            print(f"\n{Fore.YELLOW}--- Results ---{Style.RESET_ALL}")
            print(f" Country     : {data.get('country')}")
            print(f" Region      : {data.get('regionName')}")
            print(f" City        : {data.get('city')}")
            print(f" ISP         : {data.get('isp')}")
            print(f" Organization: {data.get('org')}")
        else:
            print(f"{Fore.RED}[!] Failed to fetch location data.{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
        
    input(f"\n{Fore.CYAN}[Press Enter to return to main menu]{Style.RESET_ALL}")

def dns_lookup():
    clear_screen()
    banner()
    domain = input(f"{Fore.YELLOW}[?] Enter Domain (e.g., example.com): {Style.RESET_ALL}")
    if not domain:
        return
        
    print(f"\n{Fore.BLUE}[*] Gathering basic info for {domain}...{Style.RESET_ALL}")
    try:
        ip = socket.gethostbyname(domain)
        print(f"{Fore.GREEN}[+] Primary IP: {ip}{Style.RESET_ALL}")
        
        # Using crt.sh public certificate logs for subdomains/DNS info as a lightweight method
        print(f"{Fore.BLUE}[*] Checking public certificate logs for subdomains...{Style.RESET_ALL}")
        url = f"https://crt.sh/?q=%.{domain}&output=json"
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            subdomains = set()
            for entry in res.json():
                name_value = entry.get('name_value')
                if name_value:
                    for sub in name_value.split('\n'):
                        subdomains.add(sub.strip())
            print(f"\n{Fore.GREEN}[+] Found {len(subdomains)} unique subdomains/entries:{Style.RESET_ALL}")
            for sub in list(subdomains)[:15]: # Show first 15
                print(f"    - {sub}")
        else:
            print(f"{Fore.YELLOW}[!] Could not fetch crt.sh logs.{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")

    input(f"\n{Fore.CYAN}[Press Enter to return to main menu]{Style.RESET_ALL}")

def about():
    clear_screen()
    banner()
    print(f"{Fore.WHITE}  ReconSpect is an automated reconnaissance and OSINT tool")
    print(f"  designed for cybersecurity enthusiasts and ethical hackers.")
    print(f"  Developed by Tajim Uddin for educational and authorized testing.{Style.RESET_ALL}")
    input(f"\n{Fore.CYAN}[Press Enter to return to main menu]{Style.RESET_ALL}")

if __name__ == '__main__':
    while True:
        choice = main_menu()
        if choice == '01' or choice == '1':
            ip_lookup()
        elif choice == '02' or choice == '2':
            ip_lookup()
        elif choice == '03' or choice == '3':
            dns_lookup()
        elif choice == '99':
            about()
        elif choice == '00' or choice == '0':
            print(f"\n{Fore.GREEN}Exiting... Happy Hacking!{Style.RESET_ALL}\n")
            sys.exit(0)
        else:
            print(f"{Fore.RED}[!] Invalid Option!{Style.RESET_ALL}")
            time.sleep(1)
