from browserist import Browser
from _config.browser_settings import default
from _helper import external_url

class TestGetCurrentUrl():
    def test_get_current_url(self) -> None:
        with Browser(default.HEADLESS) as browser:
            browser.open.url(external_url.EXAMPLE_COM)
            assert browser.get.url.current() == "http://example.com/"