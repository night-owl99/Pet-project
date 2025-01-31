from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link) 
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    
def test_correct_name_of_the_product_in_add_to_basket_confirmation(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link) 
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_the_correct_product_name_in_message()
    
def test_correct_price_of_the_product_in_basket_price_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link) 
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_the_correct_product_price_in_message()