from _config.timeout_settings import DEFAULT_NO_TIMEOUT

from browserist import BrowserSettings, BrowserType

DEFAULT = BrowserSettings(
    type=BrowserType.OPERA,
    timeout=DEFAULT_NO_TIMEOUT
)

HEADLESS = BrowserSettings(
    type=BrowserType.OPERA,
    headless=True,
    timeout=DEFAULT_NO_TIMEOUT
)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    type=BrowserType.OPERA,
    headless=True,
    disable_images=True,
    timeout=DEFAULT_NO_TIMEOUT
)
