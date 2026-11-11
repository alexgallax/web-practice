from playwright.sync_api import expect

from web_practice.pages.dashboard_page import DashboardPage

LOW_GLUCOSE_LEVEL_WITH_ALARM = "2"
EXPECTED_GLUCOSE_LEVEL = "2.0"


class TestUI:

    def test_ui(self, pump_id: str, dashboard_page: DashboardPage):
        (
            dashboard_page
            .open()
            .fill_pump_input(pump_id)
            .click_pump_button()
            .fill_glucose_input(LOW_GLUCOSE_LEVEL_WITH_ALARM)
            .click_glucose_button()
        )
        expect(dashboard_page.glucose_level).to_have_text(EXPECTED_GLUCOSE_LEVEL)
