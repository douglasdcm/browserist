from browserist import Browser


def test_close_window(browser_default_headless_scope_function: Browser) -> None:
    browser = browser_default_headless_scope_function
    number_of_window_handles_1 = browser.window.handle.count(selenium=True)
    browser.window.open.new_window()
    number_of_window_handles_2 = browser.window.handle.count(selenium=True)
    browser.window.close()
    number_of_window_handles_3 = browser.window.handle.count(selenium=True)

    assert number_of_window_handles_1 == 1
    assert number_of_window_handles_2 == 2
    assert number_of_window_handles_3 == 1


def test_close_tab(browser_default_headless_scope_function: Browser) -> None:
    browser = browser_default_headless_scope_function
    number_of_window_handles_1 = browser.window.handle.count(selenium=True)
    browser.window.open.new_tab()
    number_of_window_handles_2 = browser.window.handle.count(selenium=True)
    browser.window.close()
    number_of_window_handles_3 = browser.window.handle.count(selenium=True)

    assert number_of_window_handles_1 == 1
    assert number_of_window_handles_2 == 2
    assert number_of_window_handles_3 == 1
