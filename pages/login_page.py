from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "The url is not for the login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
    
    def register_new_user(self, email, password):
        email_address = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        email_address.send_keys(email)
        
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        password_field.send_keys(password)
        
        confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM_FIELD)
        confirm_password_field.send_keys(password)
        
        send_button = self.browser.find_element(*LoginPageLocators.REGISTER_SEND_BUTTON)
        send_button.click()