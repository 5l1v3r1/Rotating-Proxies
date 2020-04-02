from selenium import webdriver
import time
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from colorama import Fore, Back, Style
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Rotating Proxies")
print(ascii_banner)


proxy_array = []

with open(r'p.txt') as my_file:
    for list in my_file:
        proxy_array.append(list)

print(Fore.GREEN + 'Fetching proxies...')

converted_proxies = []

for element in proxy_array:
    converted_proxies.append(element.strip())


print(Fore.WHITE + 'Proxies are ready for automated testing.\n\nInitiating...')


for prox in converted_proxies:
    PROXY = prox
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL",

    }
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-insecure-localhost')
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(75)
    index = converted_proxies.index(prox)
    try:
        #Change website
        driver.get('https://www.google.com')
        try:
            h1 = driver.find_element_by_css_selector('h1')
            if h1.text == u"This site can’t be reached" or h1.text == u"No Internet":
                print(Fore.RED + 'Faulty Proxy','/ ',len(converted_proxies))
                driver.quit()
            else:

                
                # Write Selenium code

                
                print(Fore.GREEN + 'Used:', index + 1 ,'/ ',len(converted_proxies))
                driver.quit()
        except NoSuchElementException:
            pass
    except TimeoutException:
        print(Fore.RED + 'TimeoutException','/ ',len(converted_proxies))
        driver.quit()


print(Fore.WHITE + 'Done.')
