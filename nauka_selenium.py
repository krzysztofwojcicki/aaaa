import unittest
from selenium import webdriver


class nauka_seleniumRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://onet.pl#/")



    def testWrongEmail(self):
        driver = self.driver

        zaloguj_btn = WebDriverWait(driver, 60)\
        .until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        zaloguj_btn.click()




        sleep(5)

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
