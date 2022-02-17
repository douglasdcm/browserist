from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from ..wait.for_element import wait_for_element
from ...exception.element import NoElementFoundException
from ...exception.timeout import WaitForElementTimeoutException

def input_clear(driver: object, xpath: str) -> None:
    wait_for_element(driver, xpath)
    try:
        input_field = driver.find_element(By.XPATH, xpath)
        input_field.clear()
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, xpath) from TimeoutException
    except NoSuchElementException:
        raise NoElementFoundException(driver, xpath) from NoSuchElementException
