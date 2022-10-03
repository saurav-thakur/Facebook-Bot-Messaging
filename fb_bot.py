import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


# I am using brave browser as my browser so you can change this according to the Browser
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
Path = 'F:\\Python\\Selenuim\\chromedriver.exe'

print(brave_path)
print(Path)

option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument("--disable-notifications")
option.add_argument("--start-maximized")
driver = webdriver.Chrome(Path, options=option)

driver.get('https://www.facebook.com')

username = driver.find_element(By.ID,"email")
username.send_keys(" ") ## Enter your username

password = driver.find_element("name","pass")
password.send_keys(" ") ## Enter Your Password


login = driver.find_element("name","login")
# login.send_keys(Keys.RETURN)
login.click()

time.sleep(10)


message_click = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[2]/div[4]/div[1]/div[2]/span/span/div/div[1]")
message_click.click()

search_msg = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div/div/label/input")
search_msg.send_keys("Gaurav Thakur")
time.sleep(10)
search_msg.send_keys(Keys.DOWN)
search_msg.send_keys(Keys.DOWN, Keys.RETURN)

time.sleep(5)


## Looping the message
# for i in range(5):
#     type_msg = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p")
#     type_msg.send_keys("Brooooooooo")
#     type_msg.send_keys(Keys.RETURN)

type_msg = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p")
type_msg.send_keys("This is a bot message")
type_msg.send_keys(Keys.RETURN)

