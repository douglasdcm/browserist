from selenium.webdriver.common.by import By

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def get_texts(browser_driver: BrowserDriver, xpath: str, timeout: int) -> list[str]:
    xpath = XPath(xpath)
    wait_for_element(browser_driver.webdriver, browser_driver.settings, xpath, timeout)
    driver = browser_driver.get_webdriver()
    elements: list[object] = driver.find_elements(By.XPATH, xpath)  # type: ignore
    return [element.text for element in elements]  # type: ignore
