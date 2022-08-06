from selenium.webdriver.common.by import By

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def switch_to_iframe(browser_driver: BrowserDriver, xpath: str, timeout: float) -> None:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    driver = browser_driver.get_webdriver()
    iframe_element = driver.find_element(By.XPATH, xpath)  # type: ignore
    driver.switch_to.frame(iframe_element)  # type: ignore
