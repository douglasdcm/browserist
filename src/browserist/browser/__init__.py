__all__ = []

from typing import Union
from ..helper import get
from .open import Open
from ..model.browser.base.driver import BrowserDriver
from ..model.browser.base.settings import BrowserSettings
from ..model.browser.base.type import BrowserType
from ..model.extension.internet_explorer import InternetExplorerBrowserExtension
from ..model.extension.safari import SafariBrowserExtension

class Browser:
    """Main class of Browserist that sets the Selenium web driver and contains all helper functions."""

    def __init__(self, settings: Union[BrowserSettings, None] = None) -> None:
        """Initiates the browser driver whether the settings calls for Chrome, Firefox, etc."""

        self._browser_driver: BrowserDriver = get.browser_driver(settings)
        self.driver: object = self._browser_driver.webdriver
        
        match self._browser_driver.settings.type:
            case BrowserType.INTERNET_EXPLORER:
                self.ie: InternetExplorerBrowserExtension = InternetExplorerBrowserExtension(self._browser_driver)
            case BrowserType.SAFARI:
                self.safari: SafariBrowserExtension = SafariBrowserExtension(self._browser_driver)
            case _:
                pass

        self.open: Open = Open(self._browser_driver)

    def get(self, url: str) -> None:
        """Open page."""

        self.driver.get(url)
    
    def back(self) -> None:
        """Press the browser's back button."""

        self.driver.back()

    def forward(self) -> None:
        """Press the browser's forward button."""

        self.driver.forward()

    def refresh(self) -> None:
        """Refresh the current page."""

        self.driver.refresh()

    def quit(self) -> None:
        """Close web driver."""

        self.driver.quit()
