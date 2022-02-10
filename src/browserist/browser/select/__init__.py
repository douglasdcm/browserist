from .input_field import select_input_field
from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods

class SelectDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def input_field(self, xpath: str) -> None:
        """Select input field, similar to clicking the mouse on a form field."""

        select_input_field(self._driver, xpath)
