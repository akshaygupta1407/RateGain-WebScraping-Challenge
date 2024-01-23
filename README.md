# RateGain-WebScraping-Challenge
#**Overview**
This project involves web scraping a website to extract specific data fields such as blog title, date, image URL and likes count from each page. The obtained data will be stored in a Python dictionary and converted into a data frame for analysis. 

#**Setup**
Before starting the web scraping process, it's important to set up the necessary libraries and infrastructure. The following libraries will be used:
requests: for handling HTTP requests
BeautifulSoup: for parsing HTML content
pandas: for data manipulation and analysis

**Web Scraping Function**
The scrape_page() function defines the web scraping process. It inputs the base URL and returns a dictionary containing the extracted data fields.

Web Scraping Process
To start the web scraping process, run the following command:
python `webScrap.py`
This will iterate through every page on the website and extract the specified data fields for each page. The extracted data will be stored in the scraped_data dictionary.

**Results**
Once the web scraping process is complete, you can view the results on the `output.csv` file.

Website: https://rategain.com/blog/
