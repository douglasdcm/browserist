from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods
from .element import get_screenshot_of_element
from .visible_portion import get_screenshot_of_visible_portion


class ScreenshotDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def element(self, xpath: str, file_name: str | None = None, destination_dir: str | None = None) -> None:
        """Take screenshot of visible portion and save as PNG image. Default destination directory is from where the script is executed. Examples:

        browser.screenshot.element("/element/xpath") # Default file name and destination

        browser.screenshot.element("/element/xpath", "image.png") # Custom file name and default destination

        browser.screenshot.element("/element/xpath", "image.png", "./screenshots") # Custom file name and destination

        browser.screenshot.element("/element/xpath", destination_dir = "./screenshots") # Default file name and custom destination

        Note that "/element/xpath" should be a valid XPath expression."""

        get_screenshot_of_element(self._driver, xpath, self._settings, file_name, destination_dir)

    def visible_portion(self, file_name: str | None = None, destination_dir: str | None = None) -> None:
        """Take screenshot of visible portion and save as PNG image. Default destination directory is from where the script is executed. Examples:

        browser.screenshot.visible_portion() # Default file name and destination

        browser.screenshot.visible_portion("image.png") # Custom file name and default destination

        browser.screenshot.visible_portion("image.png", "./screenshots") # Custom file name and destination

        browser.screenshot.visible_portion(destination_dir = "./screenshots") # Default file name and custom destination"""

        get_screenshot_of_visible_portion(self._driver, self._settings, file_name, destination_dir)
