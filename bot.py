from time import sleep #importing all required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from google import google
import sys
import random

def send_msg(msg,driver): #function to send messages
	try:
		element = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/footer//div[contains(@class,"pluggable-input-body")]')
		element.click() #find the textfield to send messages and click it
		element.send_keys(msg) #fill it with message and send the message
		element.send_keys(Keys.RETURN)
		#print "Message sent"
	except:
		print "Message sending failed"
	
def callapi(headers,driver):#function to call Messages API
	apilink = "https://ajith-messages.p.mashape.com/getMsgs?category="
	i = random.randint(1,3)
	if i == 1: #here three categories of messages are randomly sent to avoid boring the receiver of the messages
		apilink = apilink + "love"
	if i == 2:
		apilink = apilink + "sweet"
	if i == 3:
		apilink = apilink + "friendship"
	try :
		response = requests.get( apilink, headers=headers ).json() # request API
		send_msg(response["Message"]+". Will you be my valentine?",driver)
	except:
		print "Can't call Messages API"

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")
sleep(1)

headers={ "X-Mashape-Key": <'YOUR API KEY'>, "Accept": "application/json" } #replace the <'YOUR API KEY'> with your generated API key
moments=['non-empty moments list'] #write and fill some short happy moments with him/her
songs=['non empty songs list'] #write and fill some popular love song names

while True:
	try :
		element = driver.find_element_by_xpath('//div[@id="pane-side"]//span[contains(@title,"<VALENTINES NAME>")]') #replace name of your valentine here
		element.click() #select chat. This is repeated to select chat repeatedly to avoid falter even if another chat is selected
		all_text_msg = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div/div/div[3]').text.split("\n") #retrieve last sent message
		if 'yes' not in all_text_msg[-2].lower().split(" ") or 'ha' not in all_text_msg[-2].lower().split(" ") : #check if last sent message is a 'Yes' to your last proposal
			rint = random.randint(1,3)
			if rint == 1:
				msg = random.choice(moments) + ". Will you be my valentine?" #send random happy moments
				send_msg(msg,driver)
			if rint == 2:
				searchstring = random.choice(songs) + " youtube" #select random song name
				googleresults = google.search(searchstring,1) #search Youtube results for the song in Google
				searchlink = googleresults[0].link #retrieve the first link
				msg = searchlink + " .I dedicate this song to you. Will you be my valentine?"
				send_msg(msg,driver) #dedicate it
			if rint == 3:
				callapi(headers,driver)
			sleep(25)
		else:
			print "Proposal Accepted" #end if proposal is accepted. Job done
			break
	except:
		print "Something went wrong"
		continue
