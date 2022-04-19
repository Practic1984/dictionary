from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
 
 
option = webdriver.ChromeOptions()
option.add_argument('headless')
 
city = input()
 
driver = webdriver.Chrome(chrome_options=option)
driver.get('https://www.gismeteo.by/')
 
search = driver.find_element_by_xpath('//*[@id="js-search"]')
search.send_keys(city)
sleep(10)
search.send_keys(Keys.ENTER)
 
weather = driver.find_element_by_xpath('/html/body/section/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/a[1]/div/div[1]/div[3]/div[1]/span[1]/span')
print(weather.text + " Сейчас в " + city)
 
driver.quit()