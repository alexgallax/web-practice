from decimal import Decimal, ROUND_HALF_UP


def round_glucose_value_as_dashboard(value: int) -> str:
    return str(Decimal(str(value)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
