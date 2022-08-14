from _helper.timeout import reset_to_not_timed_out

from browserist import Browser


def test_get_all_window_handles(browser_default_headless_scope_function: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_scope_function)
    assert len(browser.window.handle.all(selenium=True)) == len(browser.window.handle.all(selenium=False)) == 1
    browser.window.open.new_tab()
    assert len(browser.window.handle.all(selenium=True)) == len(browser.window.handle.all(selenium=False)) == 2
    browser.window.open.new_window()
    assert len(browser.window.handle.all(selenium=True)) == len(browser.window.handle.all(selenium=False)) == 3
