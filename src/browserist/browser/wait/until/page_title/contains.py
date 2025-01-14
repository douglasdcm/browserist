from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore

from .....exception.timeout import WaitForPageTitleToChangeTimeoutException
from .....helper.timeout import set_is_timed_out, should_continue
from .....model.browser.base.driver import BrowserDriver


def wait_until_page_title_contains(browser_driver: BrowserDriver, page_title_fragment: str, timeout: float) -> None:
    try:
        driver = browser_driver.get_webdriver()
        WebDriverWait(driver, timeout).until(EC.title_contains(page_title_fragment))
    except TimeoutException:
        browser_driver.settings = set_is_timed_out(browser_driver.settings)
        if not should_continue(browser_driver.settings):
            raise WaitForPageTitleToChangeTimeoutException(browser_driver, page_title_fragment) from TimeoutException
    except Exception:
        browser_driver.settings = set_is_timed_out(browser_driver.settings)
        if not should_continue(browser_driver.settings):
            raise WaitForPageTitleToChangeTimeoutException(browser_driver, page_title_fragment) from Exception
