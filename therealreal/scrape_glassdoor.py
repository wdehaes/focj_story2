from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

base_url = 'https://www.glassdoor.com/Reviews/The-RealReal-Reviews-E729017_P{}.htm'
filepath = 'data/links.txt'
driver = webdriver.Firefox()
PAUSE_TIME = 5
for i in range(1, 32):
  url = base_url.format(str(i))
  file_name = 'glassdoor_reviews_{}.html'.format(str(i))
  driver.get(url)
  driver.implicitly_wait(PAUSE_TIME)
  with open(file_name, 'w') as f:
      f.write(driver.page_source)

# for element in elements[:10]:
#     print(element)
#     print(element.get_attribute('href'))
#     element.screenshot("foo.png")
#     element.click()
#     driver.implicitly_wait(5)
#     print(driver.current_url)
#     soup = BeautifulSoup(driver.page_source, 'lxml')
#     name = soup.find('div',
#                      attrs={'class': lambda e: e.startswith(name_css) if e else False})
#     print(name)
#     # try:
#     #   element = WebDriverWait(driver, 10).until(
#     #     EC.presence_of_element_located((By.CLASS_NAME, name_css))
#     #   )
#     #   soup = BeautifulSoup(driver.page_source, 'lxml')
#     #   name = soup.find("div", class_=name_css)
#     #   print(name)
#     # finally:
#     # driver.quit()
#     driver.execute_script("window.history.go(-1)")
# assert "No results found." not in driver.page_source

driver.close()




