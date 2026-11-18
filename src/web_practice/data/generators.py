from datetime import datetime, timezone

from web_practice.api.models.send_single_telemetry_request import SendSingleTelemetryRequest

LOW_GLUCOSE_LEVEL_WITH_ALARM = 2

def low_glucose_level_payload() -> SendSingleTelemetryRequest:
    return SendSingleTelemetryRequest(
        glucose_value=LOW_GLUCOSE_LEVEL_WITH_ALARM,
        glucose_unit="mmol/L",
        timestamp=datetime.now(timezone.utc),
    )
