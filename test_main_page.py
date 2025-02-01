from pages.main_page import BasePage
from pages.login_page import LoginPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link) 
        page.open()
        page.go_to_login_page()
        
    def test_should_be_login_page(self, browser):
        
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
    