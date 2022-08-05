from ... import screenshot_helper
from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.screenshot import ScreenshotType
from ...model.type.file_png import FilePNG
from ...model.type.xpath import XPath
from ..get.element import get_element


def get_screenshot_of_element(browser_driver: BrowserDriver, xpath: str, file_name: str | None = None, destination_dir: str | None = None) -> None:
    xpath = XPath(xpath)
    if file_name is not None:
        file_name = FilePNG(file_name)
    file_name = screenshot_helper.controller.mediate_file_name(file_name, ScreenshotType.ELEMENT)
    destination_dir = screenshot_helper.controller.mediate_destination_dir(browser_driver.settings, destination_dir)
    file_path = screenshot_helper.file.get_path(destination_dir, file_name)
    element = get_element(browser_driver, xpath, timeout.DEFAULT)
    screenshot_helper.save_element(element, file_path)
