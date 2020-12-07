# car_scraper
Web scraping and machine learning application for autotrader.ca

This purpose of this application is to scrape autotrader.ca for newest car ads and identify advantageous/disadvantageous pricing.<br>
Can also be used by sellers to appraise their car.<br>
<br>
Could also be repurposed for housing prices.<br>
<br>
Steps:<br>

Connecting to target website
Retrieving data 
Populating dataframe with scraped data
Train/test/split
Saving model to determine VALUE
Building HTML page
Input field contains search parameters
Search: 
    Returns top 10 results (KPI == VALUE)
    Compares those top 10 to best VALUE of like vehicles in last week/month/year
Appraisal: 
    Intake form with details, inputs to ML model and gets price output. 



