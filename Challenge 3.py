import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/andrewlynn/PycharmProjects/untitled/Challenges/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        self.driver.get("https://www.copart.com/")
        popular = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")
        for elements in popular:
            print(elements.text + ": " + elements.get_attribute("href"))


if __name__ == '__main__':
    unittest.main()
