from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ..wait.for_element import wait_for_element

def check_if_is_element_enabled(driver: object, xpath: str) -> bool:
    wait_for_element(driver, xpath)
    try:
        element = driver.find_element(By.XPATH, xpath)
        return element.is_enabled()
    except NoSuchElementException:
        return False
