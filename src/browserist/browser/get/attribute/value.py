from selenium.webdriver.common.by import By

from ....constant import timeout
from ...wait.for_element import wait_for_element


def get_attribute_value(driver: object, xpath: str, attribute: str, timeout: int = timeout.DEFAULT) -> str:
    wait_for_element(driver, xpath, timeout)
    return driver.find_element(By.XPATH, xpath).get_attribute(attribute)
