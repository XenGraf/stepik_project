from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "login form is not presened"

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "register form is not presened"
        
    def register_new_user(self, email, password):
        input1 = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        input3.send_keys(password)
        button1 = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        button1.click()
        
    def should_be_success_registration_message(self):
        message = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        message_text = message.text()
        print(message_text)
        assert message_text == "Thanks for registering!","registration failed"
                
                    
                    
                        
