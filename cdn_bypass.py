import socket
import os
from colorama import Fore
from colorama import Style
import time
class Cloud_flare_by_pass():
    def __init__(self):
        self.Domain = None
    def subdomain_check(self):
        os.system('cls')
        sub_domains = ['www','new','mail','remote','blog','webmail','server','ns1','ns2','smtp','secure','vpn','m','shop','ftp','mail2','test','portal','ns','ww1','host','support','dev','web','bbs','ww42','mx','mail1','2','forum','owa','gw','admin','store','mx1','cdn','api','exchange','app','gov','2tty','vps','govyty','news']
        for sub_d in sub_domains:
            try:
                s = socket.gethostbyname(f'{sub_d}.{self.Domain}')
                print(f'{Fore.LIGHTWHITE_EX}{sub_d}.{self.Domain} ip --------> {Style.RESET_ALL}{Fore.GREEN} {s}')
            except:
                pass
        print('\n')
        print(f'{Style.RESET_ALL}{Fore.LIGHTBLUE_EX}its done!!!')
    def set_domain(self,domain):
        self.Domain = domain
C = Cloud_flare_by_pass()
domain = input('enter your domain(with out subdomain): ')
C.set_domain(domain)
C.subdomain_check()
while True:
    time.sleep(1)



