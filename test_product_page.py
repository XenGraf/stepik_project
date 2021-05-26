from .pages.product_page import ProductPage
import time

def test_guest_should_see_product_url(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
   #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_url
    
def test_guest_should_be_able_to_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    page = ProductPage(browser, link)
    page.open()
    page.should_can_add_product()
    page.solve_quiz_and_get_code()
    
def test_product_should_be_added_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_can_add_product()
    page.solve_quiz_and_get_code2()
    time.sleep(5)
    page.should_match_product_names()
    page.should_match_product_prices()
    
def test_product_name_in_basket_should_correct(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_can_add_product()
    page.solve_quiz_and_get_code2()
    time.sleep(5)
    page.should_match_product_names()
    
def test_product_price_in_basket_should_correct(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_can_add_product()
    page.solve_quiz_and_get_code2()
    time.sleep(5)
    page.should_match_product_prices()
