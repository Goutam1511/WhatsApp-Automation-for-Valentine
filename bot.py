from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from google import google
import sys
import random

def send_msg(msg,driver):
	try:
		element = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/footer//div[contains(@class,"pluggable-input-body")]')
		element.click()
		element.send_keys(msg)
		element.send_keys(Keys.RETURN)
		#print "Message sent"
	except:
		print "Message sending failed"
	
def callapi(headers,driver):
	apilink = "https://ajith-messages.p.mashape.com/getMsgs?category="
	i = random.randint(1,3)
	if i == 1:
		apilink = apilink + "love"
	if i == 2:
		apilink = apilink + "sweet"
	if i == 3:
		apilink = apilink + "friendship"
	try :
		response = requests.get( apilink, headers=headers ).json()
		send_msg(response["Message"]+". Will you be my valentine?",driver)
	except:
		print "Can't call Messages API"

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")
sleep(1)

headers={ "X-Mashape-Key": "IJW6kuTHHkmshZwYVVAC5kFRvqadp1tix0OjsnnAsrAnQ7ZHRv", "Accept": "application/json" }
moments=['non-empty moments list'] #fill some happy moments with him/her
songs=['non empty songs list'] #fill some popular love song names

while True:
	try :
		element = driver.find_element_by_xpath('//div[@id="pane-side"]//span[contains(@title,"Bachchar IEM CSE A")]')
		element.click()
		all_text_msg = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div/div/div[3]').text.split("\n")
		if 'yes' not in all_text_msg[-2].lower().split(" ") or 'ha' not in all_text_msg[-2].lower().split(" ") :
			rint = random.randint(1,3)
			if rint == 1:
				msg = random.choice(moments) + ". Will you be my valentine?"
				send_msg(msg,driver)
			if rint == 2:
				searchstring = random.choice(songs) + " youtube"
				googleresults = google.search(searchstring,1) 
				searchlink = googleresults[0].link 
				msg = searchlink + " .I dedicate this song to you. Will you be my valentine?"
				send_msg(msg,driver)
			if rint == 3:
				callapi(headers,driver)
			sleep(25)
		else:
			print "Proposal Accepted"
			break
	except:
		print "Something went wrong"
		continue
