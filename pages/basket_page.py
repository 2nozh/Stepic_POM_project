from pages.base_page import BasePage
from .locators import BasketPageLocators
class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "there are items in basket"
    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE), "notifying message not present"
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.MESSAGE).text, "notifying message wrong"