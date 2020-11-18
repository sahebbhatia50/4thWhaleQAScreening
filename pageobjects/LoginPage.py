#This Class acts as a Repository for Login Page where we list out all the Web Elements and the actions that can be performed for the same
class Login():
    enter_link_text      = "ENTER"
    user_button_xpath    = "//span[@data-event-label='User']"
    login_button_linktext = "LOG IN"
    username_textbox_id = "username"
    password_textbox_id  = "password"
    submit_button_id     = "submit"
    logout_button_linktext = "LOGOUT"
    homepageheader_text_xpath = "//div[h1='My Rabbit's Account']"

# This defines the Constructor of the class
    def __init__(self, driver):
        self.driver = driver

# Action to click on Enter button
    def click_enter(self):
        self.driver.find_element_by_link_text(self.enter_link_text).click()

    # Action to click on UserIcon button
    def click_user(self):
        self.driver.find_element_by_xpath("//span[@data-event-label='User']").click()

    # Action to click on Login button
    def click_loginicon(self):
        self.driver.find_element_by_link_text(self.login_button_linktext).click()

    # Action to enter username
    def enter_username(self, name):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(name)

    # Action to enter Password
    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    # Action to click on Submit button
    def click_submit(self):
        self.driver.find_element_by_id(self.submit_button_id).click()

    # Action to click on Logout button
    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_button_linktext).click()
