import logging
import re

from PageObjects.Cqube_UI.pm_poshan import PmPoshan
from TestCases.conftest import ConfTest
from Utilities import CustomLogger
from Utilities.ReadProperties import ReadConfig


class TestPmPoshan:
    pm_poshan = None
    driver = None

    @classmethod
    def setup(cls):
        cls.driver = ConfTest.get_driver()
        cls.pm_poshan = PmPoshan(cls.driver)
        cls.pm_poshan.open_cqube_application()
        cls.logger = CustomLogger.setup_logger('Program_PM_Poshan', ReadConfig.get_logs_directory() + "/Program.log",
                                               level=logging.DEBUG)

    def test_navigation_to_pm_poshan_dashboard(self):
        self.logger.info("*************** Tc_cQube_PM_Poshan_001 Testing started *****************")
        self.pm_poshan.click_dashboard()
        if 'dashboard' in self.driver.current_url:
            self.logger.info("*************** Navigation to Dashboard Screen *****************")
            assert True
        else:
            self.logger.error("********************* Navigation to Dashboard failed from PM Poshan ***********")
            assert False
        self.pm_poshan.click_pm_poshan()
        if 'poshan' in self.driver.current_url or self.driver.page_source:
            self.logger.info("********* PM Poshan Dashboard is displayed in the UI ***************")
            assert True
        else:
            self.logger.error("******** PM Poshan Menu Button is not working  *************")
            assert False
        self.logger.info("*************** Tc_cQube_PM_Poshan_001 Testing ending *****************")

    def test_validate_poshan_state_card_metrics(self):
        self.logger.info("*************** Tc_cQube_PM_Poshan_002 Testing started *****************")
        self.pm_poshan.click_pm_poshan()
        state_info = self.pm_poshan.get_vanity_card_info()
        state_value = self.pm_poshan.get_vanity_card_value()
        pm_state_value = re.sub('\D', "", state_value)
        status_title = self.pm_poshan.get_vanity_card_label()
        if state_info is not None and status_title is not None:
            self.logger.info("*********** PM Poshan Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** Nishtha Card Values is Missing ************")
            assert False
        if int(pm_state_value) > 0 and pm_state_value is not None:
            self.logger.info("*********** PM Poshan Card Values is showing ***************")
            assert True
        else:
            self.logger.error("*************** PM Poshan Card Values is Missing ************")
            assert False
        self.logger.info("*************** Tc_cQube_PM_Poshan_002 Testing ending *****************")

    @classmethod
    def teardown(cls):
        cls.driver.close()
