from _helper import screenshot
from _mock_data.screenshot import CUSTOM_SCREENSHOT_DIRECTORY, CUSTOM_SCREENSHOT_FILENAME
from _mock_data.url import internal_url
from py.path import local

from browserist import Browser

MINIMUM_FILE_SIZE = 60_000


def test_firefox_get_screenshot_of_complete_page_1(browser_firefox_headless_screenshot: Browser, tmpdir: local) -> None:
    """Test of browser.screenshot.visible_portion() with default file name and destination."""

    browser = browser_firefox_headless_screenshot
    browser.open.url(internal_url.W3SCHOOLS_COM)
    browser.screenshot.visible_portion()
    assert screenshot.images_have_minimum_file_size(tmpdir, MINIMUM_FILE_SIZE)


def test_firefox_get_screenshot_of_complete_page_2(browser_firefox_headless_screenshot: Browser, tmpdir: local) -> None:
    """Test of browser.screenshot.visible_portion("image.png") with custom file name and default destination."""

    browser = browser_firefox_headless_screenshot
    browser.open.url(internal_url.W3SCHOOLS_COM)
    browser.screenshot.visible_portion(CUSTOM_SCREENSHOT_FILENAME)
    assert screenshot.images_have_minimum_file_size(tmpdir, MINIMUM_FILE_SIZE)


def test_firefox_get_screenshot_of_complete_page_3(browser_firefox_headless_screenshot: Browser, tmpdir: local) -> None:
    """Test of browser.screenshot.visible_portion("image.png", "./screenshots") with custom file name and destination."""

    browser = browser_firefox_headless_screenshot
    browser.open.url(internal_url.W3SCHOOLS_COM)
    temp_dir = str(tmpdir.mkdir(CUSTOM_SCREENSHOT_DIRECTORY))
    browser.screenshot.visible_portion(CUSTOM_SCREENSHOT_FILENAME, temp_dir)
    assert screenshot.image_has_minimum_file_size(temp_dir, CUSTOM_SCREENSHOT_FILENAME, MINIMUM_FILE_SIZE)


def test_firefox_get_screenshot_of_complete_page_4(browser_firefox_headless_screenshot: Browser, tmpdir: local) -> None:
    """Test of browser.screenshot.visible_portion(destination_dir = "./screenshots") with default file name and custom destination."""

    browser = browser_firefox_headless_screenshot
    browser.open.url(internal_url.W3SCHOOLS_COM)
    temp_dir = str(tmpdir.mkdir(CUSTOM_SCREENSHOT_DIRECTORY))
    browser.screenshot.visible_portion(destination_dir=temp_dir)
    assert screenshot.images_have_minimum_file_size(temp_dir, MINIMUM_FILE_SIZE)
