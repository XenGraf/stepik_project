from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_add_to_basket_btn(self):
        self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_BUTTON)
    
    def should_be_review_btn(self):
        self.browser.find_element(*ProductPageLocators.REVIEW_BUTTON)
        
    def should_can_add_product(self):
        basket_button = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_BUTTON)
        basket_button.click()
        
    def should_be_product_url(self):
        assert "?promo=newYear" in self.browser.current_url
        
    def should_match_product_names(self):
        input1 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        input1_text = input1.text
        input2 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        input2_text = input2.text
        assert input2_text == input1_text, f"Wrong product name in basket, got {input2_text} instead of {input1_text}, {self.browser.current_url}"
        
    def should_match_product_prices(self):
        input1 = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        input1_text = input1.text
        input2 = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        input2_text = input2.text
        assert input2_text == input1_text, f"Wrong product price in basket, got {input2_text} instead of {input1_text} "
