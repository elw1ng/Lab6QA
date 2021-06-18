import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.color import Color
import unittest

def search(browser,search_term):
    time.sleep(3)
    browser.find_element_by_css_selector('[placeholder="Search Items..."]').send_keys(search_term)
    time.sleep(1)
    browser.find_element_by_css_selector('[placeholder="Search Items..."]').send_keys(Keys.RETURN)
    time.sleep(1)
    browser.find_element_by_css_selector('[class="btn search-btn"]').click()
    time.sleep(1)

class TradeTest(unittest.TestCase):
    def setUp(self) -> None:
        url = "https://www.pathofexile.com/trade"
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get(url)


    def test_01(self):
        search_term = "ASdsdsd"
        search(self.browser,search_term)
        actual_text = self.browser.find_element_by_xpath('//*[@id="trade"]/div[6]/div[1]/h3').text
        expected_text = "No results found"
        time.sleep(1)
        assert actual_text == expected_text
        time.sleep(2)


    def test_02(self):
        search_term = "Chaos Orb"
        search(self.browser,search_term)
        actual_text = self.browser.find_element_by_xpath('//*[@id="trade"]/div[6]/div[1]/h3').text
        expected_text = "Showing"
        assert expected_text in actual_text

    def test_03(self):
        search_term = "Headhunter Leather Belt"
        search(self.browser,search_term)
        rgb = self.browser.find_element_by_xpath('//*[@id="trade"]/div[6]/div[2]/div[1]/div[2]/div/div/div[1]/div[1]').value_of_css_property('color')
        actual_color = Color.from_string(rgb).hex
        expected_color = '#af6025'
        assert actual_color == expected_color

    def tearDown(self) -> None:
            self.browser.quit()

if __name__ == "__main__":
    unittest.main()

