import time
from src.browserist import Browser

browser = Browser()

time.sleep(1)

browser.get("https://github.com/jakob-bagterp/")
browser.get("https://www.dr.dk")
browser.back()
browser.forward()
browser.refresh()

browser.quit()
