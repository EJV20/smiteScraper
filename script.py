import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from random import seed
from random import randint

godUrl = "https://www.smitefire.com/smite/gods"
itemUrl = "https://www.smitefire.com/smite/items"

chromeDriver = "C:\\Users\\jvitu\Downloads\\chromedriver_win32\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromeDriver)
driver.get("https://www.smitefire.com/smite/gods")

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

godTeam = []
if sys.argv[1] is not None:
    num_team = int(sys.argv[1])
    i = 0
    while i < num_team:
        seed()
        x = randint(0, len(gods) - 1)
        newGod = gods[x]
        if newGod not in godTeam:
            godTeam.append(newGod)
            i += 1
else:
    seed()
    x = randint(0, len(gods) - 1)
    godTeam.append(gods[x])


for gt in godTeam:
    print(gt)

driver.close()