# EverydayTasksAutomation
Automation for daily routine tasks using python selenium

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Selenium Version](https://img.shields.io/badge/selenium-3.14-blue.svg)](https://www.seleniumhq.org)

Everyday task automation is windows application for automating everyday tasks such as Gmail, Amazon, Facebook.
![Automation Home Page](/screenshots/AutomationHomeWindow.png)

Automation script is written in python selenium with GUI build with wxpython.

## Features

* Gmail automation: Log in to user account, overview all mails and logout from gmail account.


* Amazon automation: Fetch amazon products details from pre configured products.
![Amazon Products automation](/screenshots/amazonProducts.png)

* Facebook automation: Log in to facebook, send birthday greeting to friends and logout.

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone git@github.com:umaimagit/EverydayTasksAutomation.git
```

Install the requirements:

```bash
pip install selenium
```


```bash
pip install wxpython
```

Finally, run the script:

```bash
python EverydayTasksGUI.py
```

## License

The source code is released under the MIT License.
