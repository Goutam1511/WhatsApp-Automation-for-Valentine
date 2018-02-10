from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

def send_msg(msg,driver):
	element = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/footer//div[contains(@class,"pluggable-input-body")]')
	element.click()
	element.send_keys(msg)
	element.send_keys(Keys.RETURN)
	print "Message sent"

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")
sleep(5)

headers={ "X-Mashape-Key": "IJW6kuTHHkmshZwYVVAC5kFRvqadp1tix0OjsnnAsrAnQ7ZHRv", "Accept": "application/json" }
while True:
	element = driver.find_element_by_xpath('//div[@id="pane-side"]//span[contains(@title,"Ritushree")]')
	element.click()
	response = requests.get("https://ajith-messages.p.mashape.com/getMsgs?category=friendship", headers=headers ).json()
	send_msg(response["Message"],driver)
	sleep(25)
