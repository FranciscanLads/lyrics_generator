from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = None

try:
    driver = webdriver.Chrome()
    action=ActionChains(driver)
    driver.get("https://www.azlyrics.com/t/twentyonepilots.html")
    driver.implicitly_wait(2)
    links = driver.find_elements_by_xpath("//*[@id='listAlbum']")
    driver.implicitly_wait(2)
    try:
        element = WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.ID, "listAlbum")))
    finally:
        with open("twentyonepilots"+".html", "w", encoding="utf8") as f:
            f.write(driver.page_source)

finally:
    if driver is not None:
        driver.close()