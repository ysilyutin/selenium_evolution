import unittest
from selenium import webdriver


class SmokeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        cls.driver.get("https://testmunk.com/login")

    def test_verify_amount_of_testruns(self):
        # Get the email and password textboxes
        self.email_field = self.driver.find_element_by_name("email")
        self.email_field.clear()

        self.password_field = self.driver.find_element_by_name("password")
        self.password_field.clear()

        self.sign_in_button = self.driver.find_element_by_id("log-in")

        # Enter valid email\password and click Sign In button
        self.email_field.send_keys("*****@testmunk.com")
        self.password_field.send_keys("****")
        self.sign_in_button.click()

        # Find amount of testruns on the page
        testruns = self.driver.find_elements_by_class_name("run-name-input")

        print("Found " + str(len(testruns)) + " testruns.")

        for testrun in testruns:
            print(testrun.text)

    @classmethod
    def tearDownClass(cls):
        # Close the browser window
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main(verbosity=2)