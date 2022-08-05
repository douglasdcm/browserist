import time

from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.combo_settings.login_credentials import LoginCredentials
from ...model.combo_settings.login_form import LoginForm1Step, LoginForm2Steps
from ..click.button import click_button
from ..input.value import input_value
from ..open.url_if_not_current import open_url_if_not_current
from ..wait.for_element import wait_for_element
from ..wait.until.url.contains import wait_until_url_contains


def combo_log_in(browser_driver: BrowserDriver, login_credentials: LoginCredentials, login_form: LoginForm1Step | LoginForm2Steps) -> None:
    # TODO: Incorporate timeout strategy and settings
    # TODO: Handle timeout.DEFAULT in alignment with timeout strategy and settings

    def login_form_1_step(browser_driver: BrowserDriver, login_form: LoginForm1Step) -> None:
        input_value(browser_driver, login_form.username_input_xpath, login_credentials.username, timeout.DEFAULT)
        input_value(browser_driver, login_form.password_input_xpath, login_credentials.password, timeout.DEFAULT)
        click_button(browser_driver, login_form.submit_button_xpath, timeout.DEFAULT)

    def login_form_2_steps(browser_driver: BrowserDriver, login_form: LoginForm2Steps) -> None:
        input_value(browser_driver, login_form.username_input_xpath, login_credentials.username, timeout.DEFAULT)
        click_button(browser_driver, login_form.username_submit_button_xpath, timeout.DEFAULT)
        input_value(browser_driver, login_form.password_input_xpath, login_credentials.password, timeout.DEFAULT)
        click_button(browser_driver, login_form.password_submit_button_xpath, timeout.DEFAULT)

    if login_form.url is not None:
        open_url_if_not_current(browser_driver, login_form.url)

    if type(login_form) is LoginForm1Step:
        login_form_1_step(browser_driver, login_form)
    elif type(login_form) is LoginForm2Steps:
        login_form_2_steps(browser_driver, login_form)

    if login_form.post_login_wait_seconds is not None:
        time.sleep(login_form.post_login_wait_seconds)
    if login_form.post_login_url_contains is not None:
        wait_until_url_contains(browser_driver, login_form.post_login_url_contains, timeout.DEFAULT)
    if login_form.post_login_element_xpath is not None:
        wait_for_element(browser_driver, login_form.post_login_element_xpath, timeout.DEFAULT)
