from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import config as cfg

chromedriver = cfg.cfg["chromedriver"]
ops = Options()
ops.add_argument('--headless')
ops.add_argument('--disable_gpu')
ops.add_argument('--log-level=3')

def scrape_gods():
    godUrl = "https://www.smitefire.com/smite/gods"

    print(chromedriver)

    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=ops)
    driver.get(godUrl)

    i = 1
    elem = "init"
    gods = []
    while elem != None:
        try:
            elem = driver.find_element_by_xpath("//*[@id=\"foot\"]/div[1]/div[2]/a[" + str(i) + "]")
            if "error" not in str(elem.text).lower():
                gods.append(elem.text)
            i += 1

        except:
            break

    driver.close()
    return gods



def scrape_items():
    itemUrl = "https://www.smitefire.com/smite/items"

    driver = webdriver.Chrome(executable_path=chromedriver)
    driver.get(itemUrl)

    i = 1
    elem = "init"
    gods = []
    while elem != None:
        try:
            elem = driver.find_element_by_xpath("//*[@id=\"foot\"]/div[1]/div[2]/a[" + str(i) + "]")
            if "error" not in str(elem.text).lower():
                gods.append(elem.text)
            i += 1

        except:
            break

    driver.close()
