from selenium.webdriver.common.by import By

from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def input_clear(driver: object, xpath: str, timeout: int) -> None:
    xpath = XPath(xpath)
    wait_for_element(driver, xpath, timeout)
    input_field_element = driver.find_element(By.XPATH, xpath)  # type: ignore
    input_field_element.clear()
