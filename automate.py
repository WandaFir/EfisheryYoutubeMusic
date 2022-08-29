from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Using Chrome to access web
path = "C:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(path)

# Open the website
driver.get('https://music.youtube.com/')
driver.maximize_window()

search_icon = driver.find_element(By.CLASS_NAME, 'tp-yt-paper-icon-button')
search_icon.click()

search_input = driver.find_element(By.CLASS_NAME, 'ytmusic-search-box').find_element(By.CSS_SELECTOR, 'input')
search_input.click()
search_input.send_keys('jkt48 flying high') #diganti sesuai judul lagu yang mau dicari
search_input.send_keys(Keys.ENTER)

wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/ytmusic-shelf-renderer[1]/div[1]/h2/yt-formatted-string')))
result = driver.find_element(By.XPATH, '//*[@id="contents"]/ytmusic-responsive-list-item-renderer/div[2]/div[1]/yt-formatted-string/a')
result.click()