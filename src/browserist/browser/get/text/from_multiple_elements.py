from selenium.webdriver.common.by import By
from typing import List
from ...wait.for_element import wait_for_element
from ....constant import timeout

def get_text_from_multiple_elements(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> List[str]:
    wait_for_element(driver, xpath, timeout)
    elements = driver.find_elements(By.XPATH, xpath)
    return [element.text for element in elements]
