
#
# from selenium.webdriver.common import utils


from src.all_imports import *


class LoginPage(BasePage):
    """
    Page Factory for login page.
    """
    # Locators
    sign_in_link = "//a[@class='login']"
    email_input = "//input[@id='email']"
    password_input = "//input[@id='passwd']"
    sign_in_button = "//button[@id='SubmitLogin']"
    sign_out_link = "//a[@class='logout']"
    message_xpath = ""
    email_create_input = "//input[@id='email_create']"
    create_account_button = "//button[@id='SubmitCreate']"


    # methods
    def click_sign_in_link(self):
        self.click_element_by_xpath(self.sign_in_link)
        time.sleep(2)


    def enter_email(self,email):
        self.enter_text_by_xpath(self.email_input, email)
        utils.LOG.info(f"email entered {email}")

    def enter_password(self, password):
        self.enter_text_by_xpath(self.password_input, password)
        utils.LOG.info(f"email entered {password}")



    def click_sign_in_button(self):
        self.click_element_by_xpath(self.click_sign_in_button)
        utils.LOG.info("Sign in button clicked.")
        time.sleep(5)


    def sign_out(self):
        self.click_element_by_xpath(self.sign_out_link)
        utils.LOG.info("Signed out from the website.")



    def get_app_message(self):
        return self.get_text_by_xpath(self.message_xpath)



class AccountCreationPage(BasePage):
    pass

    def select_title(self, title):
        """

        :param title: 'Mr' or 'Mrs'
        :return:
        """
        pass
