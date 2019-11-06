from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
base_url = 'https://www.mercari.com/'
search_url = 'https://www.mercari.com/search/?categoryIds=22&facets=2&itemConditions=2-3-4-5&length=30&minPrice=20000'
driver = webdriver.Firefox()
driver.get(search_url)
name_css = "ItemInfo__ProductNameText"
elements = driver.find_elements_by_css_selector(
    "a.Link__StyledPlainLink-dkjuk2-2")


SCROLL_PAUSE_TIME = 5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
pid = 1
while True and pid < 1000:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    pid = pid + 1
    if pid % 5 == 0:
      page = 'html/page_{}.html'.format(str(pid/5))
      with open(page, 'w') as f:
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
