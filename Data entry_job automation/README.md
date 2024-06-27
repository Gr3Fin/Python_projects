# Data Entry Automation

> Looking for a bicykle for my child, so she could learn how to ride a bike, I came up with an idea to automize my search process a little bit
> and store bike offers that match my requirements in google sheets with Python.
---
Skills and Tools Covered:
#### - Data scraping with BeautifulSoap
#### - Data insert with selenium 
#### - Data filtering with pandas 
---
**NOTE**:
1. Due to constant changes in offers on websites like this it may be necessary to update  
search options in _data.py_ with time (like the URL the data is scraped from).  
2. At first, create a Google Form on Google Drive as Short answer  
  and put the link to the Form in _form_fill.py_ (changes to the input fields references will be necessary).
3. Comment the part of code with browser window open/close if desired.
---
Files structure:
* form_fill.py - _enter collected data in Google Form (selenium)_
* data.py - _data scraping (BeautifulSoap)_
* process_data.py - _filter scraped data (pandas)_
---
Useful links:
- [Google Forms](https://www.google.com/forms/about/)
- [Selenium](https://selenium-python.readthedocs.io/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)
- [Pandas](https://pandas.pydata.org/docs/user_guide/index.html)
