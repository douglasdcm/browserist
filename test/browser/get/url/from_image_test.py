import pytest
from _helper import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected", [
    (internal_url.W3SCHOOLS_COM, "//*[@id='bgcodeimg2']/div/img",
     f"{internal_url.W3SCHOOLS_COM_DIR}/how-spaces-works3.png"),
    (internal_url.W3SCHOOLS_COM, "//*[@id='Frontend']/img", f"{internal_url.W3SCHOOLS_COM_DIR}/codeeditor.gif"),
    (internal_url.W3SCHOOLS_COM, "//*[@id='Backend']/img", f"{internal_url.W3SCHOOLS_COM_DIR}/best2.gif"),
])
def test_get_url_from_image(url: str, xpath: str, expected: str, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    assert browser.get.url.from_image(xpath) == expected
