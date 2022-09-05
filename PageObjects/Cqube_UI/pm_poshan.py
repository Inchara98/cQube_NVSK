from selenium.webdriver.common.by import By

from PageObjects.Cqube_UI.BasePage import Base
from Utilities.ReadProperties import ReadConfig


class PmPoshan(Base):

    """Locators for dashboard and pm poshan"""

    dashboard_button = (By.ID, 'menu-item-0')
    pm_poshan_button = (By.ID, 'menu-item-4')
    pm_poshan_i_tag = (By.XPATH, "//app-nutrition-health/div[1]/div/div[1]/sb-cqube-info-card/div/img")
    pm_poshan_vanity_card_value = (By.XPATH, "//app-nutrition-health/div[1]/div/div["
                                             "1]/sb-cqube-info-card/div/div/span[1]")
    pm_poshan_vanity_card_label = (By.XPATH, "//app-nutrition-health/div[1]/div/div["
                                             "1]/sb-cqube-info-card/div/div/span[2]")

    def __init__(self, driver):
        super().__init__(driver)

    """This function is used to open the cQube application"""
    def open_cqube_application(self):
        self.get_url(ReadConfig.get_application_url())

    """This function is used to click on the cQube dashboard"""
    def click_dashboard(self):
        self.click(self.dashboard_button)

    """This function is used to click on the PM Poshan button"""
    def click_pm_poshan(self):
        self.click(self.pm_poshan_button)

    """This function is used to get the vanity card i-tag information"""
    def get_vanity_card_info(self):
        return self.get_attribute_value('title', self.pm_poshan_i_tag)

    """This function is used to get the vanity card values or metrics"""
    def get_vanity_card_value(self):
        return self.get_web_element_text(self.pm_poshan_vanity_card_value)

    """This function is used to get the vanity card label"""
    def get_vanity_card_label(self):
        return self.get_web_element_text(self.pm_poshan_vanity_card_label)
