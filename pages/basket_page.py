from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def shouldnt_be_products_in_basket(self):
            assert self.is_not_element_present(*BasePageLocators.BASKET_LINK), "Products are present in the basket (but they shouldn't)"

    def should_be_message_about_empty_basket(self):
            assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), "There is no empty basket message!"