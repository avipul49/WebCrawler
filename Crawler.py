from selenium import webdriver
import time
import FormPage
import Flight
import ResultPage
import CSVHelper
loop = 3 # do it 3 times
timeInterval = 10 # run in every 10 sec
while loop > 0:
    driver = webdriver.Firefox()
    #driver = webdriver.PhantomJS()
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
    driver.quit() 
    loop = loop - 1
    time.sleep(timeInterval)