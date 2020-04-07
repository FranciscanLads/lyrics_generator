from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup


with open("coldplay.html", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    code_soup = soup.findAll("div", {"class": "listalbum-item"})
    for i in code_soup:
        a = i.find('a', href=True)
        b= "https://www.azlyrics.com"+a['href'][2:]
        print("\""+b+"\""+",\n")

