from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
url = "https://sis.nyu.edu/psc/csprod/EMPLOYEE/SA/c/NYU_SR.NYU_CLS_SRCH.GBL"
timeout = 30

for i in range(909):
    print(f"started scraping page {i} of 909")
    if i == 10:
        break

    driver = webdriver.Chrome("/Users/anthonyardisukotjo/Downloads/chromedriver", options=options)
    driver.get(url)

    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, "NYU_CLS_DERIVED_DESCR50lbl")))
    except TimeoutException:
        print('Timed out waiting for page to load')
        driver.quit()
    driver.execute_script(f"submitAction_win0(document.win0,'LINK1${i}');")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "RESULT_COUNTlbl")))
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    title = soup.find(id="RESULT_COUNTlbl").get_text()
    with open(f"./data/{title}.html", "w") as o:
        o.write(page_source)
    print(f"finished scraping page {i} of 909")
    driver.close()

print("done")