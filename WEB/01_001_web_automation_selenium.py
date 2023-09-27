from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt
import requests

service = ChromeService("C:\Development\chromedriver.exe")


def get_driver(links):
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(links)
    return driver


def get_motivation():
    driver = get_driver("https://automated.pythonanywhere.com/")
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text


def get_temperature():
    driver = get_driver("https://automated.pythonanywhere.com/")
    time.sleep(3)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return (element.text).split(": ")[1]


def get_login():
    driver = get_driver("https://automated.pythonanywhere.com/login/")
    driver.find_element(by='id', value='id_username').send_keys("automated")
    time.sleep(2)
    driver.find_element(by='id', value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by='xpath', value="/html/body/nav/div/a").click()
    time.sleep(3)
    return driver.current_url


def login_and_temperature():
    driver = get_driver("https://automated.pythonanywhere.com/login/")
    driver.find_element(by='id', value='id_username').send_keys("automated")
    time.sleep(2)
    driver.find_element(by='id', value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by='xpath', value="/html/body/nav/div/a").click()
    time.sleep(3)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    print((element.text).split(": ")[1])
    driver.close()
    driver.quit()


def get_temp_and_save_txt():
    driver = get_driver("https://automated.pythonanywhere.com/")
    time.sleep(3)
    while True:
        text = ((driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")).text).split(": ")[1]
        name = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
        with open(name, 'w') as file:
            file.write(text)
        time.sleep(3)


def titan22_login():
    driver = get_driver("https://titan22.com/account/login?return_url=%2Faccount")
    driver.find_element(by="id", value="CustomerEmail").send_keys("halimovhalimjon420@gmail.com")
    time.sleep(2)
    driver.find_element(by="id", value="CustomerPassword").send_keys("Halimjon420" + Keys.RETURN)
    time.sleep(2)
    framename = driver.findElement(By.tagName("iframe")).getAttribute("name")
    driver.switchTo().frame(framename)
    driver.findElement(by="xpath", value="//span[@id='recaptcha-anchor']").click()
    driver.find_element(by="xpath",
                        value="/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
    time.sleep(5)
    driver.close()
    driver.quit()


def get_csv_file_from_yahoo():
    ticker = input("Enter the ticket symbol: ").upper()         # TSLA
    from_date = input("Enter start date in yyyy/mm/dd format: ")    # 2010/06/29
    to_date = input("Enter end date in yyyy/mm/dd format: ")    # 2023/09/22

    from_datetime = dt.strptime(from_date, "%Y/%m/%d")
    to_datetime = dt.strptime(to_date, "%Y/%m/%d")

    from_epoch = int(time.mktime(from_datetime.timetuple()))
    to_epoch = int(time.mktime(to_datetime.timetuple()))

    print(from_epoch, to_epoch, ticker)

    link = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36'}
    content = requests.get(url=link, headers=headers).content
    print(content)
    with open('data.csv', 'wb') as file:
        file.write(content)


get_csv_file_from_yahoo()
