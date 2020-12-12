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


def add_to_dict(driver, path, d, key, god):
    val = ""
    try:
        elem = driver.find_element_by_xpath(path)
        val = elem.text
    except:
        print("Attribute: " + key + " failed for god: " + god)
        val = ""
        
    if key == "type":
        x = val.split(",")
        if len(x) == 2:
            d["attack"] = x[0]
            d["power"] = x[1]
    else:
        d[key] = val
    return d


def get_list_of_gods():
    f = open("godList.txt", "r")
    lines = f.readlines()

    gods = []
    for line in lines:
        gods.append(line)

    return gods


def scrape_gods_plus():
    print("Scrape_gods_plus")
    gods = get_list_of_gods()

    god_dict = {}
    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=ops)
    for god in gods:
        godUrl = "https://smite.gamepedia.com/" + god
        print(godUrl)
        driver.get(godUrl)

        new_dict = {}
        new_dict = add_to_dict(driver, "//*[@id=\"mw-content-text\"]/div/table[1]/tbody/tr[4]/td/b", new_dict, "title", god)
        new_dict = add_to_dict(driver, "//*[@id=\"mw-content-text\"]/div/table[1]/tbody/tr[5]/td/a", new_dict, "pantheon", god)
        new_dict = add_to_dict(driver, "", new_dict, "attack", god)
        new_dict = add_to_dict(driver, "", new_dict, "power", god)
        new_dict = add_to_dict(driver, "", new_dict, "class", god)
        new_dict = add_to_dict(driver, "", new_dict, "difficulty", god)
        new_dict = add_to_dict(driver, "", new_dict, "released", god)

        god_dict[god] = new_dict

    print(god_dict)
