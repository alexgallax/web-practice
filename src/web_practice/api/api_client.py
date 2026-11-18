import allure
import requests
from requests import Response

from web_practice.api.models.send_single_telemetry_request import SendSingleTelemetryRequest


class ApiClient:

    def __init__(self):
        self._BASE_URL = "https://ips.alexgallax-edu.ru"

    @allure.step("Отправка единичного значения телеметрии для помпы {pump_id}: {payload}")
    def send_single_telemetry(self, pump_id, payload: SendSingleTelemetryRequest) -> Response:
        path = f"api/v1/pumps/{pump_id}/telemetry"
        return requests.post(
            url=f"{self._BASE_URL}/{path}",
            json=payload.model_dump(mode="json"),
        )
