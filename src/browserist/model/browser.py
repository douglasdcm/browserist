from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, unique
from selenium.webdriver import ChromeOptions, FirefoxOptions, FirefoxProfile
from typing import Union

@unique
class BrowserType(Enum):
    """Class to define browser type, e.g. Chrome, Firefox, etc."""
    
    CHROME = "Chrome"
    FIREFOX = "Firefox"

@dataclass    
class BrowserSettings:
    """Class to configure the browser driver."""
    
    type: BrowserType = BrowserType.CHROME
    headless: bool = False
    disable_images: bool = False

class BrowserClass(ABC):
    """Abstract class that contains the web driver based on browser type and configuration."""
    
    def __init__(self, settings: Union[BrowserSettings, None] = None) -> None:
        """Initiates basic properties of the browser and web driver."""
        
        self.settings = BrowserSettings() if settings is None else settings 
        self.chrome_options: ChromeOptions = ChromeOptions()
        self.firefox_options: FirefoxOptions = FirefoxOptions()
        self.firefox_profile: FirefoxProfile = FirefoxProfile()
        if settings is None:
            self.ensure_browser_type()
        self.set_options_and_profile()
        self.driver: object = self.set_webdriver()

    def set_options_and_profile(self) -> None:
        self.disable_images()
        self.enable_headless()

    @abstractmethod
    def ensure_browser_type(self) -> None:
        """Method to ensure the correct browser type if a specific browser instance is created directly from a subclass (e.g. ChromeBrowser, FirefoxBrowser, etc.) without the optional settings as argument."""
        
        raise NotImplementedError

    @abstractmethod
    def disable_images(self) -> None:
        """Method to configure web driver to disable download of images for faster browsing."""
        
        raise NotImplementedError

    @abstractmethod
    def enable_headless(self) -> None:
        """Method to enable headless version of web driver (i.e. don't open browser window) for faster browsing."""

        raise NotImplementedError

    @abstractmethod
    def set_webdriver(self) -> object:
        """Method to set web driver based on settings."""

        raise NotImplementedError
