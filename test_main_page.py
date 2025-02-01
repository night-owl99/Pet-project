from pages.main_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

def test_guest_can_go_to_login_page(browser):
    
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link) 
    page.open()
    page.go_to_login_page()
    
def test_should_be_login_page(browser):
    
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link) 
    page.open()
    page.should_be_login_url()
    
def test_login_form_is_present(browser):
    
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link) 
    page.open()
    page.should_be_login_form()
    
def test_register_form_is_present(browser):
    
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link) 
    page.open()
    page.should_be_register_form()
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link) 
    page.open()
    page.go_to_basket_page()
    page.shouldnt_be_products_in_basket()
    page.should_be_message_about_empty_basket()
    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.shouldnt_be_products_in_basket()
    page.should_be_message_about_empty_basket()
    