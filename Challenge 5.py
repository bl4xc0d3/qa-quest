import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/andrewlynn/PycharmProjects/untitled/Challenges/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        self.driver.get("https://www.copart.com/")
        self.driver.find_element(By.ID, "input-search").send_keys("porsche")
        self.driver.find_element(By.XPATH, "//*[@id=\"search-form\"]/div/div[2]/button").click()
        self.driver.implicitly_wait(3)
        for elements in self.driver.find_elements(By.XPATH, "//table[@id='serverSideDataTable']/tbody/tr/td[6]/span["
                                                            "@data-uname='lotsearchLotmodel']"):
            print(elements.get_attribute("innerText"))


if __name__ == '__main__':
    unittest.main()
