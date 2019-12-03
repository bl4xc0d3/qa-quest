import unittest
import time
from selenium import webdriver



class Challenge2 (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/andrewlynn/PycharmProjects/untitled/Challenges/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com/")
        self.driver.set_window_size(1366, 947)

        self.driver.find_element_by_id("input-search").click()
        self.driver.find_element_by_id("input-search").send_keys("exotics")
        self.driver.find_element_by_css_selector(".btn-lightblue:nth-child(1)").click()
        time.sleep(3)
        self.assertIn("PORSCHE", self.driver.find_element_by_id("serverSideDataTable").text)


if __name__ == '__main__':
    unittest.main()


