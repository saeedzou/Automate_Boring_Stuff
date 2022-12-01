# Automate Boring Stuff

This repository contains programs that automate everyday boring tasks.

## Setup

You should download the latest [selenium driver](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) for your browser. I used Microsoft Edge in my implementations, so you'll have to change the webdriver to your browser. The webdriver also needs to be added to PATH.
To run a program just run it as a python file.

### Requirements

```text
selenium
requests
notify_run
notifypy
```

## Contents

### [login_SUT_py_requests.bat](https://github.com/saeedzou/Automate_Boring_Stuff/blob/master/login_SUT_py_requests.bat)

This program logs into the SUT login network page using python requests. It uses the requests module to send a POST request to the login page. To execute this program download [login_SUT_py_requests.bat](https://github.com/saeedzou/Automate_Boring_Stuff/blob/master/login_SUT_py_requests.bat) and [login_SUT_py_requests.py](https://github.com/saeedzou/Automate_Boring_Stuff/blob/master/login_SUT_py_requests.py) and run the batch file.
You should also change the username and password in the python file, and the path to the python file in the batch file.

### [login_SUT_selenium.py](https://github.com/saeedzou/Automate_Boring_Stuff/blob/master/login_SUT_selenium.py)

This automates login-based networks that require credentials to be used.
Update the USERNAME and PASSWORD variables in the file to your credentials.
This is implemented using selenium.

### [Train Ticket Checker](https://github.com/saeedzou/Automate_Boring_Stuff/blob/master/train_ticket_finder_Alibaba.py)

This is a program I wrote to check for available train tickets in a price range.
It is not scalable and you're gonna have to do some updates to the url paths if you need it to work.
I will implement a notifier in a future version
