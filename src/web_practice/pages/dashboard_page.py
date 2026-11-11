from playwright.sync_api import Page


class DashboardPage:

    def __init__(self, page: Page):
        self.page = page

        self.pump_input = page.get_by_placeholder("например, student_ivanov")
        self.apply_pump_button = page.get_by_role("button", name="Применить")
        self.glucose_input = page.get_by_placeholder("glucose_value")
        self.apply_glucose_button = page.get_by_role("button", name="Отправить")
        self.glucose_level = page.locator("span.glucose-value")

    def open(self) -> DashboardPage:
        self.page.goto("https://ips.alexgallax-edu.ru/dashboard")
        return self

    def fill_pump_input(self, text: str) -> DashboardPage:
        self.pump_input.fill(text)
        return self

    def click_pump_button(self) -> DashboardPage:
        self.apply_pump_button.click()
        return self

    def fill_glucose_input(self, text: str) -> DashboardPage:
        self.glucose_input.fill(text)
        return self

    def click_glucose_button(self) -> DashboardPage:
        self.apply_glucose_button.click()
        return self
