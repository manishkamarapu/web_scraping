# web_scraping

1. install python 3.9.2 from "https://www.python.org/downloads/" and make sure it's path is added to the environmental variables.
2. Then, install any text editor such as "Visual Studio code".
3. Create virtual environment in 'VS code' using the command "python3 -m venv tutorial-env" in terminal.
4. activate virtual environment using the command "c:\>tutorial-env\Scripts\activate.bat" in terminal.
5. Now, go to view->Command palette->Select interpreter and select the above created "tutorial-env" as interpretor.
6. Create a scrapy project with command "scrapy stratproject scape_website" in terminal.
7. The above command installs all the neccessary files and folders.
8. Then create a new file "scrapy_spider.py" under "scrape_website->spiders" folder.
9. Write the code in scrapy_spider.py file with the urls of "dmoztools.net" to extract the information of website name, url, desc and title_tag.
10. Install "flake8 tool" with command "pip install flake8" in terminal and format the code using "flake8 scrapy_spider.py" command.
11. Based on the items created in scrapy_spider.py update the items.py file under "scrape_website->spider" folder.
12. Include the spiders in  _.init_.py file which has to be executed once we run the program.
13. Use command "scrapy crawl posts -o website_details.csv" to retrive the website details and store in csv file.
