#Proof of concept for NYU Course Scraper

Proof of concept of how an NYU Albert Course scraper could potentially work with Selenium and BeautifulSoup.

## How it works
1. Create a selenium web driver instance
2. Navigate to the NYU Course Search Home page
3. Run the following JavaScript Script on the driver instance
  `driver.execute_script(f"submitAction_win0(document.win0,'LINK1${i}');")` 
 Each value of i is mapped to a specific subject. 
 This javascript is what is run when the subject link is clicked on in the course home page.  
4. The webdriver waits until the element with id `RESULT_COUNTlbl` is shown. 
This is the element containing the text `1 - xx results for SUBJECTCODE | Total Class Count: xx`
5. Then extract the HTML using BeautifulSoup, parse and save the data
6. Repeat for all values of i/all subjects. There are 908 subjects in 2022/2023

## Todo:
- [ ] Parse the data returned from the scraper
- [ ] Scrape multiple pages in parallel?
- [ ] Dynamically determine total number of subjects/ max value of i from the home course page
