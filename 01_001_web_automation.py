from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time

servise = ChromeService("C:\Development\chromedriver.exe")


def get_driver(links):
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=servise, options=options)
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

