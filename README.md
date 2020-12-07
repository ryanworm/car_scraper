# car_scraper
Web scraping and machine learning application for autotrader.ca

This purpose of this application is to scrape autotrader.ca for newest car ads and identify advantageous/disadvantageous pricing.<br>
Can also be used by sellers to appraise their car.<br>
<br>
Could also be repurposed for housing prices.<br>
<br>
Steps:<br>
<br>
Connecting to target website<br>
Retrieving data<br>
Populating dataframe with scraped data<br>
Train/test/split<br>
Saving model to determine VALUE<br>
Building HTML page<br>
Input field contains search parameters<br>
Search:<br> 
    Returns top 10 results (KPI == VALUE)<br>
    Compares those top 10 to best VALUE of like vehicles in last week/month/year<br>
Appraisal:<br> 
    Intake form with details, inputs to ML model and gets price output.<br>



