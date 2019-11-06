from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def login():
  base_url = 'https://us.vestiairecollective.com/'
  driver.get(base_url)
  driver.implicitly_wait(PAUSE_TIME)
  login_button = driver.find_element_by_xpath("//*[contains(text(), 'Sign in')]")
  driver.execute_script("arguments[0].click();", login_button)
  driver.implicitly_wait(PAUSE_TIME)

  username = driver.find_element_by_id("user_email")
  password = driver.find_element_by_id("user_password")

  username.send_keys("willem.dehaes@columbia.edu")
  password.send_keys("willem")

  submit_field = driver.find_element_by_xpath("//button[@type='submit']")
  submit_field.click()
  driver.implicitly_wait(PAUSE_TIME)


PAUSE_TIME = 10
# base_url = 'https://us.vestiairecollective.com/women-bags/handbags/louis-vuitton/brown-cloth-noe-louis-vuitton-handbag-8464739.shtml'
# driver = webdriver.Firefox()
# driver.get(base_url)
# driver.implicitly_wait(PAUSE_TIME)
# login()
url = "https://us.vestiairecollective.com/we-love/women/p-0/#priceMin=20000"
for i in range(1,50):
  driver = webdriver.Firefox()
  old_p = "/p-{}/".format(str(i-1))
  new_p = "/p-{}/".format(str(i))
  url = url.replace(old_p, new_p)
  driver.get(url)
  driver.implicitly_wait(PAUSE_TIME)
  page = 'html/page_{}.html'.format(str(i))
  with open(page, 'w') as f:
    f.write(driver.page_source)
  driver.close()



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

driver.quit()
