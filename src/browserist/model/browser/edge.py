from selenium import webdriver
from .base.driver import BrowserDriver
from .base.type import BrowserType

class EdgeBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.EDGE

    def set_webdriver(self) -> object:
        return webdriver.Edge(
            options = self.edge_options)
      
    def disable_images(self) -> None:
        if self.settings.disable_images:
            self.edge_options.use_chromium = True
            preferences = {"profile.managed_default_content_settings.images": 2, "profile.default_content_settings.images": 2}
            self.edge_options.add_experimental_option("prefs", preferences)
    
    def enable_headless(self) -> None:
        if self.settings.headless:
            self.edge_options.use_chromium = True
            self.edge_options.add_argument("headless")
            self.edge_options.add_argument("disable-gpu")