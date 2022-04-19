from selenium import webdriver 
from time import sleep
driver = webdriver.Chrome()
driver.get('https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=%D1%82%D1%80%D1%83%D1%81%D1%8B+%D0%BC%D1%83%D0%B6%D1%81%D0%BA%D0%B8%D0%B5+%D0%B1%D0%BE%D0%BA%D1%81%D0%B5%D1%80%D1%8B&fdlvr=24&fbrand=51828%3B20624')
tovars = driver.find_elements_by_class_name('name')
for i in range(0, len(tovars)):
    print(tovars[i].text)
    

