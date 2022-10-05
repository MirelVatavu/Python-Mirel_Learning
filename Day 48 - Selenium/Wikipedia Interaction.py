from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions import key_actions
chrome_driver = 'D:\Python Projects\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver)

# driver.get('https://en.wikipedia.org/wiki/Main_Page')
#
# # article_count = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# #
# # article_count.click()
#
# # all_portals = driver.find_element(By.LINK_TEXT,'Boroughitis')
# # all_portals.click()
#
# search = driver.find_element(By.NAME,'search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)

# driver.get('http://dokwiki.lacon.de/dokwiki/Hauptseite')
#
# search = driver.find_element(By.NAME,'search')
# search.send_keys('1080150')
# search.send_keys(Keys.ENTER)
#
# link = driver.find_element(By.LINK_TEXT,'1080150')
# link.click()
#
# login = driver.find_element(By.LINK_TEXT,'Anmelden')
# login.click()
#
# user = driver.find_element(By.NAME,'wpName')
# user.send_keys('Mirel Vatavu')
#
# password = driver.find_element(By.NAME,'wpPassword')
# password.send_keys('myr3lL11??')
#
# login_attempt = driver.find_element(By.ID,'wpLoginAttempt')
# login_attempt.click()
#
# create_page = driver.find_element(By.LINK_TEXT,'Create')
# create_page.click()
#
# insert_template = driver.find_element(By.ID,'wpTextbox1')
# insert_template.send_keys('''
# == PCN ==
# *
#
# == Datenblatt ==
# *
#
# == Montageanleitung ==
# *
#
# == Angebot ==
# *
#
# == Konformitätsbestätigung(en) ==
# *
#
# == REACH/SVHC Nachweise ==
# *
# ''')

# driver.get('https://secure-retreat-92358.herokuapp.com/')
#
# f_name = driver.find_element(By.NAME,'fName')
# f_name.send_keys('Mirel')
#
# l_name = driver.find_element(By.NAME,'lName')
# l_name.send_keys('Vasea')
#
# email = driver.find_element(By.NAME,'email')
# email.send_keys('mirel@vasea.gmail.ro')
#
# sign_up = driver.find_element(By.CSS_SELECTOR,'form button')
# sign_up.click()