import re
from .get import get_text_from_element
from ..constant import timeout

def check_if_element_contains_text(driver: object, xpath: str, regex: str, ignore_case: bool = True, timeout: int = timeout.DEFAULT) -> bool:
	current_text = get_text_from_element(driver, xpath, timeout)
	if ignore_case:
		match = re.search(regex, current_text, re.IGNORECASE)
	else:
		match = re.search(regex, current_text)
	return bool(match)