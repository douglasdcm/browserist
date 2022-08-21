import asyncio

from ..browser.scroll.check_if.is_end_of_page import check_if_scroll_is_end_of_page
from ..browser.scroll.get.position import get_scroll_position
from ..browser.scroll.page.down import scroll_page_down
from ..browser.scroll.page.to_top import scroll_to_top_of_page
from ..browser.scroll.to_position import scroll_to_position
from ..model.browser.base.driver import BrowserDriver
from ..model.screenshot import ScreenshotTempDataHandler


def firefox(browser_driver: BrowserDriver, destination_file_path: str) -> None:
    driver = browser_driver.get_webdriver()
    driver.get_full_page_screenshot_as_file(destination_file_path)  # type: ignore


async def default(browser_driver: BrowserDriver, destination_file_path: str, destination_dir: str, delay_seconds: float) -> None:
    async def async_scroll_to_top_of_page(browser_driver: BrowserDriver, delay_seconds: float) -> None:
        scroll_to_top_of_page(browser_driver, delay_seconds=0)
        # Instead of a blocking wait/delay in the above method, let's release the working thread to do something else:
        await asyncio.sleep(delay_seconds)

    async def async_scroll_page_down(browser_driver: BrowserDriver, delay_seconds: float) -> None:
        scroll_page_down(browser_driver, delay_seconds=0)
        # Instead of a blocking wait/delay in the above method, let's release the working thread to do something else:
        await asyncio.sleep(delay_seconds)

    async def async_scroll_to_position(browser_driver: BrowserDriver, x: int, y: int, delay_seconds: float) -> None:
        scroll_to_position(browser_driver, x, y, delay_seconds=0)
        # Instead of a blocking wait/delay in the above method, let's release the working thread to do something else:
        await asyncio.sleep(delay_seconds)

    async def get_screenshot_of_visible_portion_and_scroll_down(browser_driver: BrowserDriver, handler: ScreenshotTempDataHandler, delay_seconds: float) -> None:
        handler.save_screenshot(browser_driver)
        await asyncio.gather(
            asyncio.to_thread(handler.incremental_merge_screenshot_iteration_with_complete_page, handler._iteration),
            async_scroll_page_down(browser_driver, delay_seconds),
        )
        handler.increment_iteration()

    # Save inital scroll position so we can return to it later.
    x_inital, y_initial = get_scroll_position(browser_driver)

    # Prepare for iteration from the top of the page.
    _, handler = await asyncio.gather(
        async_scroll_to_top_of_page(browser_driver, delay_seconds),
        asyncio.to_thread(
            ScreenshotTempDataHandler, destination_dir=destination_dir, destination_file_path=destination_file_path)
    )

    # Take screenshots of the visible portion until we reach the end of the page.
    await get_screenshot_of_visible_portion_and_scroll_down(browser_driver, handler, delay_seconds)
    while check_if_scroll_is_end_of_page(browser_driver) is not True:
        await get_screenshot_of_visible_portion_and_scroll_down(browser_driver, handler, delay_seconds)

    # Handle if first screenshot covers the complete page, return to initial scroll position, and tidy up temp files.
    await asyncio.gather(
        async_scroll_to_position(browser_driver, x_inital, y_initial, delay_seconds),
        handler.remove_temp_files()
    )
