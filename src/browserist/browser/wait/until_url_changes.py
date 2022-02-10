from ..get.current_url import get_current_url
from ...constant import timeout
from ... import helper

def wait_until_url_changes(driver: object, baseline_url: str, timeout: int = timeout.DEFAULT) -> None:
    def has_url_changed(driver: object, baseline_url: str) -> bool:
        return get_current_url(driver) != baseline_url

    helper.retry.until_condition_is_true(has_url_changed(driver, baseline_url), timeout)