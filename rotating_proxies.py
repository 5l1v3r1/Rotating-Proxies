from selenium import webdriver
import time
from selenium.webdriver.common.proxy import Proxy, ProxyType
import random
from colorama import Fore, Back, Style
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Rotating Proxies")
print(ascii_banner)


proxy_array = []

with open(r'p.txt') as my_file:
    for list in my_file:
        proxy_array.append(list)

print(Fore.RED + 'Fetching proxies...')

converted_proxies = []

for element in proxy_array:
    converted_proxies.append(element.strip())


print(Fore.WHITE +'Proxies are ready for automated testing.')
print('Initiating...')


for prox in converted_proxies:
    PROXY = prox
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL",

    }
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-insecure-localhost')
    driver = webdriver.Chrome(options=options)




    #SELENIUM CODE
    #driver.get('https://www.google.com/')





    time.sleep(3)
    index = converted_proxies.index(prox)
    print('Used:', index + 1 ,'/ ',len(converted_proxies))
    driver.quit()

print('Done.')
