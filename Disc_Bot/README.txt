WebScraping Discord Bot v.1.03

Requirements:
Python
Beautiful Soup Library
Discord Library
Random Library
Asyncio Library
URLLIB Library
fake_useragent Library

Use:
Ensure the above Librarys are installed along with Python 3. Run the script by using the following command line in powershell or command prompt:
python TheBot.py

Goals:
For the bot to continuously scrape given websites for stock levels of given products, then notifying select people of stock levels through Discord.

Current Progress: 
v.1.03:
Implemented simple error reporting and handling from the beautiful soup library to allow the script to run indefinitely with minimul crashes from errors and exceptions.

Previous Versions:
v. 1.02:
Seperated discord communication, webscraping and URL refreshing into seperate files to allow for easier troubleshooting and modularity.

v. 1.01:
Added value limits to Amazon links due to overpricing of amazon stock levels. 

v. 1.00:
Created WebScraping.py to scrape the HTML codes for stock levels and implemented discord functionality to notify users when stock levels are found to be different.
