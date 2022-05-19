from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods
from .for_element import wait_for_element
from .random_time import wait_random_time
from .until.__main__ import WaitUntilDriverMethods
from .until_url_changes import wait_until_url_changes
from .until_url_contains import wait_until_url_contains
from .until_url_is import wait_until_url_is


class WaitDriverMethods(DriverMethods):
    __slots__ = ["until"]

    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)
        self.until: WaitUntilDriverMethods = WaitUntilDriverMethods(browser_driver, settings)

    def for_element(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until element is ready in the DOM and/or on the screen.

        Especially useful for single-page app elements handled/modified by JavaScript, but also standard HTML that doesn't load immediately, this helper function ensures that DOM elements are ready before processing."""

        wait_for_element(self._driver, xpath, timeout)

    def random_time(self, min_seconds: int = 1, max_seconds: int = 5) -> None:
        """Randomize sleep timing to make actions look less like a bot."""

        wait_random_time(min_seconds, max_seconds)

    def until_url_changes(self, baseline_url: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the browser URL has changed from a baseline URL, e.g. after a redirect or form action. The URL is evaluated as an exact match."""

        wait_until_url_changes(self._driver, baseline_url, timeout)

    def until_url_contains(self, url_fragment: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the browser URL has changed, e.g. after a redirect. The URL variable can contain both a fragment (e.g. ?login=true) or a full URL (e.g. https://www.example.com/?login=true)."""

        wait_until_url_contains(self._driver, url_fragment, timeout)

    def until_url_is(self, url: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the browser URL has changed, e.g. after a redirect. The URL is evaluated as an exact match."""

        wait_until_url_is(self._driver, url, timeout)
