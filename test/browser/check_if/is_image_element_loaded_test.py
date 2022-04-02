import pytest
from _mock_data.url import internal_url
from selenium.webdriver.common.by import By

from browserist import Browser


@pytest.mark.parametrize("xpath, expected", [
    ("/html/body/div[3]/a[1]/i", False),
    ("//*[@id='bgcodeimg2']/div/img", True),
    ("//*[@id='Frontend']/img", True),
    ("//*[@id='Backend']/img", True),
])
def test_check_if_is_image_element_loaded(xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.W3SCHOOLS_COM)
    element = browser.driver.find_element(By.XPATH, xpath)
    assert browser.check_if.is_image_element_loaded(element) is expected
