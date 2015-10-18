import unittest
from selenium import webdriver


class SmokeTest(unittest.TestCase):

    def setUp(self):
        # Create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get("https://testmunk.com/login")

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

        if __name__ == '__main__':
            unittest.main(verbosity=2)

    def tearDown(self):
        # Close the browser window
        self.driver.quit()
