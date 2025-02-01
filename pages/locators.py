from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, '#register_form [type="email"]')
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, '#register_form [name="registration-password1"]')
    REGISTER_PASSWORD_CONFIRM_FIELD = (By.CSS_SELECTOR, '#register_form [name="registration-password2"]')
    REGISTER_SEND_BUTTON = (By.CSS_SELECTOR, '#register_form [name="registration_submit"]')
    
class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    TEXT_WITH_PROD_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) strong')
    
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    TEXT_WITH_PROD_PRICE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) strong')