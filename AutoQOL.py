# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:48:07 2022

@author: lqbia
"""


from selenium import webdriver
from selenium.webdriver.support.ui import Select

import org.openqa.selenium.support.ui.Select

driver = webdriver.Chrome()

driver.get('https://home.qol.qub.ac.uk/default.aspx')



driver.find_element_by_xpath('/html/body/div[2]/div/div/div[8]/div/div[4]/div/div[1]/div/div[4]/a').click()


room = Select(driver.find_element_by_name('building_day'))

driver.find_element_by_name('building_day')

date= Select(driver.find_element_by_css_selector('body > div:nth-child(3) > div > div:nth-child(3) > form > fieldset > table > tbody > tr > td:nth-child(2) > select'))

date.select_by_value()

body > div:nth-child(3) > div > div:nth-child(3) > form > fieldset > table > tbody > tr > td:nth-child(1) > select
room.selectByValue("LIB/G.G06");

