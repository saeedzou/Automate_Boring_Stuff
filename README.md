# Automate Boring Stuff

This repository contains programs that automate everyday boring tasks.

## Setup

You should download the latest [selenium driver](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) for your browser. I used Microsoft Edge in my implementations, so you'll have to change the webdriver to your browser. The webdriver also needs to be added to PATH.
To run a program just run it as a python file.

### Requirements

```text
selenium
requests
playsound
```

## Contents

### [login_SUT_py_requests.bat](https://github.com/saeedzou/Automate_Boring_Stuff/blob/master/login_SUT_py_requests.bat)

- Logs into the SUT login network page using python requests. To run this script automatically, you can use Windows Task Scheduler to run the batch file on event triggers. 

Follow these steps:
1. Change the USERNAME and PASSWORD command-line arguments in the batch file to your credentials.
2. Change the path to the python folder path in the batch file.
3. Create a new task in Task Scheduler.
4. In the General tab, give the task a name and description.
5. In the Triggers tab, click on New and select "On an event".
6. Choose Custom and select "Edit Event Filter"
7. In the XML tab, select "edit query manually" and confirm if a popup appears.
8. Paste the following code in the XML tab and click OK. (You can change the network ssids or add more)
```xml
<QueryList>
  <Query Id="0" Path="System">
    <Select Path="Microsoft-Windows-NetworkProfile/Operational">
*[System[(EventID=10000)]] and (
*[EventData[(Data[@Name="Name"]="Sharif-WiFi")]] or
*[EventData[(Data[@Name="Name"]="Sharif-WiFi 2")]] or
*[EventData[(Data[@Name="Name"]="EE-WLANN")]]
)
</Select>
  </Query>
</QueryList>
```
9. Click OK and OK again.
10. In the Actions tab, click on New and select "Start a program".
11. In the Program/script field, enter the path to the batch file.
12. Click OK and OK again.
13. On the Conditions tab, you can uncheck the "Start the task only if the computer is on AC power" checkbox.



### [login_SUT_selenium.py](https://github.com/saeedzou/Automate_Boring_Stuff/blob/master/login_SUT_selenium.py)

This automates login-based networks that require credentials to be used.
Update the USERNAME and PASSWORD variables in the file to your credentials.
This is implemented using selenium.

### [Train Ticket Checker](https://github.com/saeedzou/Automate_Boring_Stuff/blob/master/train_ticket_finder_Alibaba.py)

This is a program I wrote to check for available train tickets in a price range.
It is not scalable and you're gonna have to do some updates to the url paths if you need it to work.
I will implement a notifier in a future version
