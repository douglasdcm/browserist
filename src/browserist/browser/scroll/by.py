import time

from ...constant import timeout


def scroll_by(driver: object, x: int, y: int, delay_seconds: float = timeout.VERY_SHORT) -> None:
    driver.execute_script(f"window.scrollBy({x}, {y});")  # type: ignore
    time.sleep(delay_seconds)  # Small delay to ensure the view is updated.
