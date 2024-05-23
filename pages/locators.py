from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR,"#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR,"#register_form")
class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR,".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR,".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR,".product_main p.price_color")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    INFO_ALERT = (By.CSS_SELECTOR, ".alert-info")

