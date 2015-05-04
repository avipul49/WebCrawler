from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
class FormPage(object):
    def __init__(self,driver):
        self.driver = driver

    def find_by_xpath(self,locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        return element

    def fill_form(self, data):
        dd = data['departure_day'].split("/")
        ad = data['arrive_day'].split("/")
        now = datetime.datetime.now()
        amonths = (int(ad[2]) - int(dd[2]))*12 + int(ad[0]) - int(dd[0])
        dmonths = (int(dd[2]) - now.year)*12 + int(dd[0]) - now.month
        #find_by_xpath('//span[text() = "One-way"]').click()
        self.find_by_xpath('//input[@name = "from_field"]').send_keys(data['from'])
        self.find_by_xpath('//a[@rel = "'+data['from']+'"]').click()       
        # self.find_by_xpath('//a[text() = "'+data['from_name']+'"]').click()
        self.find_by_xpath('//input[@name = "to_field"]').send_keys(data['to'])
        self.find_by_xpath('//a[@rel = "'+data['to']+'"]').click()       
        #self.find_by_xpath('//a[text() = "'+data['to_name']+'"]').click()
        self.find_by_xpath('//span[text() = "Depart date"]').click()
        for x in range(0, dmonths):
            self.find_by_xpath('//a[@title = "Next"]').click()

        self.find_by_xpath('//a[text() = "'+dd[1]+'"]').click()
        #find_by_xpath('//span[@id = "return-wrap"]').click()
        time.sleep(5);
        for x in range(0, amonths):
            self.find_by_xpath('//div[@id="return-cal"]//a[@title = "Next"]').click()

        self.find_by_xpath('//div[@id="return-cal"]//a[text() = "'+ad[1]+'"]').click()
        self.find_by_xpath('//span[text() = "Points"]').click()
        return self 

    def submit(self):
        self.find_by_xpath('//input[@value = "FIND IT"]').click()
