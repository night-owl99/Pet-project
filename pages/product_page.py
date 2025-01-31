from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def click_add_to_basket_button(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()
        
    def should_be_the_correct_product_name_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.TEXT_WITH_PROD_NAME).text, \
            "The product name doesn't match with the name in the message!"
            
    def should_be_the_correct_product_price_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(*ProductPageLocators.TEXT_WITH_PROD_PRICE).text, \
            "The product price doesn't match with the basket price in the message!"
            
    def shouldnt_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.TEXT_WITH_PROD_NAME), "Success message is presented (but it shouldn't)"
        
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.TEXT_WITH_PROD_NAME), "Success message hasn't disappeared (but it should)"
        
    