# WebCrawler

## Usage
Open Crawler.py and update search fields

```(Python)
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
    driver.quit() 
    loop = loop - 1
    time.sleep(timeInterval)
```

In above code variables `loop` and `timeInterval`can be changed to run the script repeatedly after specified time interval.  

Variable `data` contains the search quesry in which fields `from`, `to`, `departure_day` and `arrive_day` can be changed.

Once done with the update, run `Crawler.py`

## Result
The result from each run of the script will be store in a file named `flightDetails_MM-DD-YYYY_HH:mm.csv`. 
In the flight list `points` and `lowestPrice` for connecting flights is in the last flight and rest of the flights will have `0` as the value for these fields.

