from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .get_size import get_viewport_size
from .height import get_viewport_height
from .set.__main__ import ViewportSetDriverMethods
from .width import get_viewport_width


class ViewportDriverMethods(DriverMethods):
    __slots__ = ["set"]

    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)
        self.set: ViewportSetDriverMethods = ViewportSetDriverMethods(browser_driver)

    def get_size(self) -> tuple[int, int]:  # type: ignore
        """Get inner width and height of the viewport in pixels. Usage:

        width, height = browser.viewport.get_size()"""

        if self._timeout_should_continue():
            return get_viewport_size(self._browser_driver)

    def height(self) -> int:  # type: ignore
        """Get inner height of the viewport in pixels."""

        if self._timeout_should_continue():
            return get_viewport_height(self._browser_driver)

    def width(self) -> int:  # type: ignore
        """Get inner width of the viewport in pixels."""

        if self._timeout_should_continue():
            return get_viewport_width(self._browser_driver)
