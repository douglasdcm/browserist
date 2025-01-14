from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .hover import mouse_hover


class MouseDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def hover(self, xpath: str, timeout: float | None = None) -> None:
        """Simulate moving the mouse cursor over the middle of an element."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            mouse_hover(self._browser_driver, xpath, timeout)
