import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = 'D:\Python Projects\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://orteil.dashnet.org/cookieclicker/')

time.sleep(15)

clicks = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[15]/div[8]/button')

cursor = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[19]/div[3]/div[6]/div[2]')

grandma = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[19]/div[3]/div[6]/div[3]')

farm = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[4]')


try:
    cookiespersecond = driver.find_element(By.ID,"cookiesPerSecond")
    print(cookiespersecond.text)
except:
    print('Exemption')

counting_clicks = 0
game_on = True
start = time.time()
while game_on:
    clicks.click()
    counting_clicks += 1
    if counting_clicks==15 or counting_clicks==30 or counting_clicks==45 or counting_clicks==60 or counting_clicks==75 or counting_clicks==90:
        cursor.click()
    elif counting_clicks==190 or counting_clicks == 203 or counting_clicks == 318 or counting_clicks == 441 or counting_clicks == 574:
        grandma.click()
    elif counting_clicks== 1676 or counting_clicks== 2941:
        farm.click()

    end = time.time()
    end_game = end - start
    if end_game >300:
        print(f'Running time: {end_game}')
        try:
            cookiespersecond = driver.find_element(By.ID, "cookiesPerSecond")
            print(f'Cookies {cookiespersecond.text}')
        except:
            print('Exemption')
        game_on = False
