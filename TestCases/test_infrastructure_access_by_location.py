import os
import time
import pytest

from PageObjects.Cqube_UI.CqubeDashboard.SchoolInfrastructure.infrastructure_access_by_location import \
    InfrastructureAccessByLocation
from PageObjects.Cqube_UI.LoginPage.LoginPage import Login
from TestCases.conftest import ConfTest


class TestInfrastructureAccessByLocation:
    driver = ConfTest.get_driver()
    lp = Login(driver)
    lp.login_to_cqube()
    obj = InfrastructureAccessByLocation(driver)
    mgmt = obj.get_managements()

    @classmethod
    def setup(cls):
        # cls.driver = ConfTest.get_driver()
        # lp = Login(cls.driver)
        # lp.login_to_cqube()
        # cls.obj = InfrastructureAccessByLocation(cls.driver)
        # mgmt = cls.obj.get_managements()
        print("")

    @pytest.mark.parametrize("management", mgmt)
    def test_districts(self, management):
        errors = []
        # self.obj.select_management(management)
        self.obj.click_on_infrastructure_map_card()
        time.sleep(5)
        self.obj.click_on_downloads()
        filename = self.obj.get_filename()
        markers = self.obj.get_markers_count()
        if markers == 0:
            errors.append("District markers are not present")
            self.obj.save_screenshot("test_district_markers.png")
        if not os.path.isfile(filename):
            errors.append("District wise csv file in not downloaded")
            self.obj.save_screenshot("test_district_download_file.png")
        if int(self.obj.get_school_count_from_csv()) != int(self.obj.get_schools_count_from_footer()):
            errors.append("Schools count is mismatched")
            self.obj.remove_file_in_downloads()
            self.obj.save_screenshot("test_district_download_csv_and_footer_schools_count_mismatched.png")
        else:
            self.obj.remove_file_in_downloads()
            print("District wise csv downloaded and csv file school count is matched with footer value")
        assert len(errors) == 0, "something went wrong in this test case"

    @classmethod
    def teardown(cls):
        cls.driver.close()
