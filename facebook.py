import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait




driver = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe')

driver.get('https://facebook.com')

elem = driver.find_element_by_id('email')
elem.send_keys('kalmus2808@gmail.com')
driver.find_element_by_id('pass').send_keys('Gkalmus123')
driver.find_element_by_id('pass').send_keys(Keys.ENTER)
driver.find_element_by_xpath('//*[//*[@id="mount_0_0_mM"]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/label/input').send_keys('siema')