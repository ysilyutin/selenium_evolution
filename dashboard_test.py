import unittest
from selenium import webdriver


class DashboardTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        cls.driver.get("https://testmunk.com/login")

    def test_verify_amount_of_testruns(self):
        # Get the email and password textboxes
        email_field = self.driver.find_element_by_name("email")
        email_field.clear()

        password_field = self.driver.find_element_by_name("password")
        password_field.clear()

        sign_in_button = self.driver.find_element_by_id("log-in")

        # Enter valid email\password and click Sign In button
        email_field.send_keys("*****@testmunk.com")
        password_field.send_keys("****")
        sign_in_button.click()

        # Find amount of testruns on the page
        testruns = self.driver.find_elements_by_class_name("run-name-input")
        self.assertEqual(len(testruns), 33)

    @classmethod
    def tearDownClass(cls):
        # Close the browser window
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main(verbosity=2)
