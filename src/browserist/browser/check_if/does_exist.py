from selenium.webdriver.common.by import By

from ...model.type.xpath import XPath


def check_if_does_exist(driver: object, xpath: str) -> bool:
    xpath = XPath(xpath)
    try:
        element = driver.find_element(By.XPATH, xpath)  # type: ignore
        return element is not None
    except Exception:
        return False
