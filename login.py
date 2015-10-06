from selenium import webdriver

# Create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://testmunk.com/login")

# Get the email and password textboxes
email_field = driver.find_element_by_name("email")
email_field.clear()

password_field = driver.find_element_by_name("password")
password_field.clear()

sign_in_button = driver.find_element_by_id("log-in")

# Enter valid email\password and click Sign In button
email_field.send_keys("*****@testmunk.com")
password_field.send_keys("****")
sign_in_button.click()

# Find amount of testruns on the page
testruns = driver.find_elements_by_class_name("run-name-input")

print("Found " + str(len(testruns)) + " testruns.")

for testrun in testruns:
    print(testrun.text)

# Close the browser window
driver.quit()
