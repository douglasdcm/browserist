import pytest
from _helper import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected", [
    (internal_url.W3SCHOOLS_COM, "//*[@id='bgcodeimg2']/div/img",
     [f"{internal_url.W3SCHOOLS_COM_DIR}/how-spaces-works3.png"]),
    (internal_url.W3SCHOOLS_COM, "//img", [
        f"{internal_url.W3SCHOOLS_COM_DIR}/codeeditor.gif",
        f"{internal_url.W3SCHOOLS_COM_DIR}/best2.gif",
        f"{internal_url.W3SCHOOLS_COM_DIR}/how-spaces-works3.png",
        f"{internal_url.W3SCHOOLS_COM_DIR}/colorpicker.png",
        f"{internal_url.W3SCHOOLS_COM_DIR}/w3lynx_200.png",
        f"{internal_url.W3SCHOOLS_COM_DIR}/w3css_templates.jpg",
        f"{internal_url.W3SCHOOLS_COM_DIR}/w3schools_logo_500_04AA6D.png",
    ]),
])
def test_get_url_from_multiple_images(url: str, xpath: str, expected: list[str], browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    assert browser.get.url.from_multiple_images(xpath) == expected