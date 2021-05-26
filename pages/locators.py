from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    EMPTY_BASKET = (By.XPATH,'//*[@id="default"]/header/div[1]/div/div[2]')
    
class BasketPageLocators():
    MESSAGE_IN_BASKET= (By.XPATH, '//*[@id="content_inner"]/p')
    
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    PRODUCT_ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    REVIEW_BUTTON = (By.ID, "write_review")
    PRODUCT_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    #(By.CSS_SELECTOR, "//div[@class='product_main']")
    PRODUCT_NAME_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    #(By.CSS_SELECTOR, "//div[@class='product_main']")
    PRODUCT_PRICE_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div.alertinner')
