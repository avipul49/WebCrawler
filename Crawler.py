from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import FormPage
import Flight
import ResultPage
import CSVHelper
loop = 3 # do it 3 times
timeInterval = 10 # run in 
while loop > 0:
    driver = webdriver.Firefox()
    driver.get("http://www.jetblue.com/")

    data = {
        'from': 'MCO',
        'to': 'EWR',
        'departure_day': '5/20/2015',
        'arrive_day' : '6/3/2015'
    }

    FormPage.FormPage(driver).fill_form(data).submit()
    allFlights = ResultPage.ResultPage(driver).collectSearchResult(data);
    
    CSVHelper.writeToCSV(allFlights)
    #driver.quit() 
    loop = loop - 1
    time.sleep(timeInterval)