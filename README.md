# Route link renaming automation on Sharepoint


<img src="https://selenium-python.com/wp-content/uploads/2017/11/cropped-logo-mini.png" width="300"/>


## Features

- Auth via AutoIt tool
- Renaming of links on sharepoint via Selenium Automation tool

## Installation

Install the dependencies:

```sh
pip install -r requirements.txt
```
## Download ChromeDriver for your Chrome version:

Open Chrome browser -> Help -> About -> watch your current version of Chrome

If your version not equal 89 download chromedriver for your version in the bottom menu and extract chromedriver.exe in project folder. 

| Chrome Driver | Link to download |
| ------ | ------ |
| WebDriver | https://chromedriver.chromium.org/downloads

## Requirement tool!

AutoIt used for pass basic http authentication whose username contains special characters like "\"

| Tool | Link to download |
| ------ | ------ |
| AutoIt | https://www.autoitscript.com/site/autoit/downloads/|


## Guide how to use AutoIT

When AutoIT tool installed on your desktop open Auth.au3 file with AutoIt Editor and write your username and password:

![](./Screenshots/Screenshot_1.png)

* Modify username and password and save script.

![](./Screenshots/Screenshot_2.png)

* Compile that script:

![](./Screenshots/Screenshot_3.png)

* Move Auth.exe file in project folder:

![](./Screenshots/Screenshot_4.png)

* Add Requirement Replacing Strings OLD -> NEW
![](./Screenshots/Screenshot_5.png)


* Run script...

```sh
python main.py
```

### **Don't minimize or close browser until the user is authenticated!**

- ✨Magic ✨

Want to contribute? Great! Waiting for pull request.

