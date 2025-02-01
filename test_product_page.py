from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest
import time
from random_word import RandomWords

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link) 
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_the_correct_product_name_in_message()
    page.should_be_the_correct_product_price_in_message()


@pytest.mark.guest_seeing_basket
class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/ru/accounts/login/')
        page.open()
        
        r = RandomWords()
        self.email = r.get_random_word() + "@fakemail.org"
        self.password = r.get_random_word() + "123456789"
        
        page.register_new_user(self.email,  self.password)
        page.should_be_authorized_user()
    
    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url)
        page.open()
        page.click_add_to_basket_button()
        page.shouldnt_be_success_message()
        
    def test_user_can_add_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, url)
        page.open()
        page.click_add_to_basket_button()
        page.should_be_the_correct_product_name_in_message()
        page.should_be_the_correct_product_price_in_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url) 
    page.open()
    page.click_add_to_basket_button()
    page.shouldnt_be_success_message()
    
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, url) 
    page.open()
    page.shouldnt_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url) 
    page.open()
    page.click_add_to_basket_button()
    page.should_disappear_success_message()
    
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()