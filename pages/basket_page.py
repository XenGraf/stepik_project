from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators
from .locators import BasketPageLocators
from .login_page import LoginPage

class BasketPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)
        
    def should_be_text_about_empty_basket(self):
        input = self.browser.find_element(*BasketPageLocators.MESSAGE_IN_BASKET)
        input_text = input.text
        assert input_text == "Your basket is empty. Continue shopping", f"There is no any message about empty basket, got {input_text}"

#    def go_to_login_page(self):
#        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#        login_link.click()
       # return LoginPage(browser=self.browser, url=self.browser.current_url)
        
#    def should_be_login_link(self):
 #       self.browser.find_element(*MainPageLocators.LOGIN_LINK), "login link is not presened"

