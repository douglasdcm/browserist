from ... import helper
from ...browser.window.handle.current import get_current_window_handle
from ...exception.window_handle import WindowHandleIdNotValidError, WindowHandleNameNotUniqueError
from .handle import WindowHandle


class WindowHandleController:
    def __init__(self, driver: object) -> None:
        self._counter: int = 1
        self._window_handles: list[WindowHandle] = [
            WindowHandle(
                name=str(self._counter),
                id=get_current_window_handle(driver),
            )]

    def add_handle(self, id: str, name: str | None = None) -> None:
        if not helper.window_handle.is_valid_id(id):
            raise WindowHandleIdNotValidError(id)
        self._counter += 1
        if name is None:
            name = str(self._counter)
        if helper.window_handle.name_already_exists(name, self._window_handles):
            raise WindowHandleNameNotUniqueError(name)
        self._window_handles.append(WindowHandle(name, id))
