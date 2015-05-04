from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import Flight

class ResultPage(object):
    def __init__(self,driver):
        self.driver = driver

    def collectSearchResult(self, data):
        fromTimes = self.driver.find_elements_by_xpath('//div[@class = "from"]//time')
        toTimes = self.driver.find_elements_by_xpath('//div[@class = "to"]//time')
        fromAirports = self.driver.find_elements_by_xpath('//div[@class = "from"]//span')
        toAirports = self.driver.find_elements_by_xpath('//div[@class = "to"]//span')
        flightNumbers = self.driver.find_elements_by_xpath('//a[@class = "flight-number"]')
        points = self.driver.find_elements_by_xpath('//div[@class = "radio price"]//span[@class = "label"]')

        i = 0
        j = 0
        allFlights = []
        ddate = ''
        for fromTime in fromTimes: 
            if data['from'] == fromAirports[i].get_attribute('innerHTML').strip():
                ddate = data['departure_day']
            if data['to'] == fromAirports[i].get_attribute('innerHTML').strip():
                ddate = data['arrive_day']

            flight = Flight.Flight()
            flight.fromAirport = fromAirports[i].get_attribute('innerHTML').strip()
            flight.to = toAirports[i].get_attribute('innerHTML').strip()
            flight.departDate = ddate
            flight.arriveDate = ddate
            flight.flightNumber = flightNumbers[i].get_attribute('innerHTML').strip()
            flight.departTime = fromTimes[i].get_attribute('innerHTML').strip()
            flight.arriveTime = toTimes[i].get_attribute('innerHTML').strip()
            flight.lowestPrice = 0
            flight.points = '0'
            flight.extraCharges = '0'
            if data['from'] == toAirports[i].get_attribute('innerHTML').strip() or data['to'] == toAirports[i].get_attribute('innerHTML').strip():
                charges = points[j].get_attribute('innerHTML').strip().split('<br>')
                flight.points = charges[0].replace('pts','').strip()
                flight.extraCharges = charges[1].strip()
                j = j + 1
            allFlights.append(flight) 
            i = i + 1

        self.driver.find_element_by_xpath('//span[text() = "Dollars"]').click()
        time.sleep(10)
        prices = self.driver.find_elements_by_xpath('//div[@class = "radio price"]//span[@class = "label"]')
        i = 0
        for flight in allFlights: 
            if flight.points != '0':
                flight.lowestPrice = prices[i].get_attribute('innerHTML').strip()
                i = i + 2
        return allFlights
