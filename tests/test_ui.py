from playwright.sync_api import expect

from web_practice.api.api_client import ApiClient
from web_practice.data.generators import low_glucose_level_payload, LOW_GLUCOSE_LEVEL_WITH_ALARM
from web_practice.pages.dashboard_page import DashboardPage
from web_practice.utils.round_digit import round_glucose_value_as_dashboard


class TestUI:

    def test_ui(self, pump_id: str, dashboard_page: DashboardPage, api_client: ApiClient):
        api_client.send_single_telemetry(pump_id, low_glucose_level_payload())

        (
            dashboard_page
            .open()
            .fill_pump_input(pump_id)
            .click_pump_button()
        )

        expect(dashboard_page.glucose_level).to_have_text(
            round_glucose_value_as_dashboard(LOW_GLUCOSE_LEVEL_WITH_ALARM)
        )
