import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

search_term = "ASdsdsd"
url = "https://www.pathofexile.com/trade"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url)
browser.implicitly_wait(30)

time.sleep(3)
browser.find_element_by_css_selector('[placeholder="Search Items..."]').send_keys(search_term)
time.sleep(1)
browser.find_element_by_css_selector('[placeholder="Search Items..."]').send_keys(Keys.RETURN)
time.sleep(1)
browser.find_element_by_css_selector('[class="btn search-btn"]').click()

time.sleep(1)

actual_text = browser.find_element_by_xpath('//*[@id="trade"]/div[6]/div[1]/h3').text
expected_text = "No results found"
time.sleep(1)
assert actual_text == expected_text
time.sleep(2)


browser.get(url)
time.sleep(2)
search_term = "Chaos Orb"

browser.find_element_by_css_selector('[placeholder="Search Items..."]').send_keys(search_term)
time.sleep(1)
browser.find_element_by_css_selector('[placeholder="Search Items..."]').send_keys(Keys.RETURN)
time.sleep(1)
browser.find_element_by_css_selector('[class="btn search-btn"]').click()
time.sleep(1)
actual_text = browser.find_element_by_xpath('//*[@id="trade"]/div[6]/div[1]/h3').text
expected_text = "Showing"
assert expected_text in actual_text

time.sleep(3)
browser.close()