from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import json

import config as cfg

chromedriver = cfg.cfg["chromedriver"]
ops = Options()
ops.add_argument('--headless')
ops.add_argument('--disable_gpu')
ops.add_argument('--log-level=3')

# url         = https://smite.gamepedia.com/List_of_gods
# god         = //*[@id="mw-content-text"]/div/table/tbody/tr[1]/td[2]/a
# pantheon    = //*[@id="mw-content-text"]/div/table/tbody/tr[1]/td[3]/a[2]
# attack type = //*[@id="mw-content-text"]/div/table/tbody/tr[1]/td[4]/a[2]
# power type  = //*[@id="mw-content-text"]/div/table/tbody/tr[1]/td[5]/a[2]
# class       = //*[@id="mw-content-text"]/div/table/tbody/tr[1]/td[6]/a[2]
# difficulty  = //*[@id="mw-content-text"]/div/table/tbody/tr[1]/td[7]
# released    = //*[@id="mw-content-text"]/div/table/tbody/tr[1]/td[10]

def get_chrome_driver(url):
    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=ops)
    driver.get(url)
    return driver


def add_to_dict(driver, url, god_dict, index, god):
    val = ""
    try:
        elem = driver.find_element_by_xpath(url)
        val = elem.text
    except:
        print("Attribute: " + index + " failed for god: " + god)
        val = ""
        
    god_dict[index] = val
    return god_dict


def scrape_gods():
    godUrl = "https://www.smitefire.com/smite/gods"
    driver = get_chrome_driver(godUrl)

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


def scrape_gods_plus():
    print("Scrape_gods_plus")
    godUrl = "https://smite.gamepedia.com/List_of_gods"
    driver = get_chrome_driver(godUrl)

    print("Obtained Driver")
    i = 1
    god = "init"
    god_dict = {}
    while god != None:
        try:
            god = driver.find_element_by_xpath("//*[@id=\"mw-content-text\"]/div/table/tbody/tr[" + str(i) +"]/td[2]/a")
            god_text = god.text
            try:
                new_dict = {}
                new_dict["index"] = str(i)
                new_dict = add_to_dict(driver, "//*[@id=\"mw-content-text\"]/div/table/tbody/tr[" + str(i) +"]/td[3]/a[2]", new_dict, "pantheon", god_text)
                new_dict = add_to_dict(driver, "//*[@id=\"mw-content-text\"]/div/table/tbody/tr[" + str(i) +"]/td[4]/a[2]", new_dict, "attack", god_text)
                new_dict = add_to_dict(driver, "//*[@id=\"mw-content-text\"]/div/table/tbody/tr[" + str(i) +"]/td[5]/a[2]", new_dict, "power", god_text)
                new_dict = add_to_dict(driver, "//*[@id=\"mw-content-text\"]/div/table/tbody/tr[" + str(i) +"]/td[6]/a[2]", new_dict, "class", god_text)
                new_dict = add_to_dict(driver, "//*[@id=\"mw-content-text\"]/div/table/tbody/tr[" + str(i) +"]/td[7]", new_dict, "difficulty", god_text)
                new_dict = add_to_dict(driver, "//*[@id=\"mw-content-text\"]/div/table/tbody/tr[" + str(i) +"]/td[10]", new_dict, "released", god_text)

                god_dict[god_text] = new_dict

            except:
                print("Attribute breaks on: " + str(i))
        except:
            print("No god at index: " + str(i))
            god = None

        i += 1

    print(god_dict)
    driver.close()
    return god_dict.keys


def scrape_items():
    itemUrl = "https://www.smitefire.com/smite/items"

    driver = get_chrome_driver(itemUrl)

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
