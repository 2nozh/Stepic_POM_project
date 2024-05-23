from pages.base_page import BasePage
from .locators import ProductPageLocators
class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
    def get_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return name
    def get_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return price
    def should_be_success_alert_with_text(self,text):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ALERT), "success alert not found"
        alert_content = self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT).text
        assert "has been added to your basket" in alert_content, "wrong message in success alert"
        assert text in alert_content, "wrong product name in success alert"
        assert f"{text} has been added to your basket." in alert_content, "total text comparing was wrong"
    def should_be_info_alert_with_text(self,text):
        assert self.is_element_present(*ProductPageLocators.INFO_ALERT), "info alert not found"
        alert_content = self.browser.find_element(*ProductPageLocators.INFO_ALERT).text
        assert "Your basket total is now" in alert_content, "wrong message in info alert"
        assert text in alert_content, "wrong product price in info alert"
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT), \
           "Success message is presented, but should not be"
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT)


