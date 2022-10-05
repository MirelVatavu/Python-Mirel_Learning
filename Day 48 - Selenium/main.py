from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_driver_path = 'D:\Python Projects\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver_path)


event_times = driver.find_elements(By.CSS_SELECTOR,'.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR,'.event-widget li a')
events = {}

for n in range(len(event_times)):
    events[n] = {
        'time':event_times[n].text,
        'name':event_names[n].text
    }

print(events)



driver.close()