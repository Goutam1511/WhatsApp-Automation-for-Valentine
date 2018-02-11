# WhatsApp-Automation-for-Valentine
This valentine impress your valentine and spread love with the power of Selenium Python using Automated WhatsApp Love messages and songs.

This is a python script to automatically send love mesages fetching them from a open-source Message API or love moments from a predefined list and songs from Google to dedicate to someone who is in your WhatsApp chatlist(in short your valentine). However the message type can be changed changing the category type of the messages. So, feel free to edit the script according to your requirements.

Documentation for Setting up :

First of all replace the <Valentine's name> in the script with the name of the person to be sent messages and this name should be provided exactly as it is in the contact. Also, change the <Your API KEY> in the headers dictionary with your generated API Key for the Messages API. 
Run the python script using the "python <filename>.py" command. 
The Whatsapp Web will open in the browser and ask to scan the QR code(This will happen each time and is yet to be fixed. Maybe next valentine :P). After scanning the QR code it will wait and then choose the required person's chat and start sending love messages and songs at an interval of the predefined time in the script.

Documentation for Dependencies :

1.1. Messages API

Retrieve random messages based on your selected category. You can use this API for text messaging applications,Status updating applications and more!!

Sign up in this web portal to use the Messages API and get an unique application key for free. paste your authentication key in the headers dictionary of the script to request for random messages.

Sign up here : https://market.mashape.com/ajith/messages

1.2. Downloading Python bindings for Selenium

You can download Python bindings for Selenium from the PyPI page for selenium package. However, a better approach would be to use pip to install the selenium package. Python 3.6 has pip available in the standard library. Using pip, you can install selenium like this:

pip install selenium

You may consider using virtualenv to create isolated Python environments. Python 3.6 has pyvenv which is almost same as virtualenv.

1.3. Drivers

Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

Failure to observe this step will give you an error selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH.

Other supported browsers will have their own drivers available. Links to some of the more popular browser drivers follow.
Chrome: 	https://sites.google.com/a/chromium.org/chromedriver/downloads
Edge: 	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Firefox: 	https://github.com/mozilla/geckodriver/releases
Safari: 	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

In this project Firefox browser is used for the whole purpose but feel free to change it as per need. 

1.4. Google Search API

Google Search API is a python based library for searching various functionalities of google. It uses screen scraping to retrieve the results, and thus is unreliable if the way google's web pages are returned change in the future. This package is currently under heavy refactoring so changes in the user interface should be expected for the time being.

For more details please visit : https://github.com/abenassi/Google-Search-API/blob/master/README.md
