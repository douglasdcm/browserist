import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("width, height", [
    (1024, 600),
    (666, 666),
])
def test_set_screen_size_headless(width: int, height: int, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.EXAMPLE_COM)
    browser.screen.set(width, height)
    width_check, height_check = browser.screen.size()
    assert width == width_check and height == height_check
