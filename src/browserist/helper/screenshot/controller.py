from ... import helper
from ...model.browser.base.settings import BrowserSettings
from ...model.screenshot import ScreenshotType


def file_name(file_name: str | None, screenshot_type: ScreenshotType | None = None) -> str:
    return helper.screenshot.default_file_name(screenshot_type) if file_name is None else file_name


def destination_dir(settings: BrowserSettings, destination_dir: str | None = None) -> str:
    if destination_dir is None:
        return settings.screenshot_dir
    helper.directory.create_if_not_exists(destination_dir)
    return helper.directory.ensure_trailing_slash(destination_dir)
