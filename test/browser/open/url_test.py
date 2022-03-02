import pytest
from _helper import external_url, internal_url

from browserist import Browser
from browserist.helper import url


@pytest.mark.parametrize("url1, url2", [
    (internal_url.EXAMPLE_COM, internal_url.W3SCHOOLS_COM),
    (internal_url.W3SCHOOLS_COM, external_url.EXAMPLE_COM),
    (external_url.EXAMPLE_COM, external_url.IANA_ORG),
])
def test_open_url(url1: str, url2: str, browser_default_headless: Browser) -> None:
    url1 = url.ensure_trailing_slash(url1)
    url2 = url.ensure_trailing_slash(url2)
    browser = browser_default_headless
    browser.open.url(url1)
    get_url1 = url.ensure_trailing_slash(browser.get.url.current())
    browser.open.url(url2)
    get_url2 = url.ensure_trailing_slash(browser.get.url.current())
    assert get_url1 == url1 and get_url2 == url2 and get_url1 != get_url2
