import time
from src.browserist import Browser

browser = Browser()

browser.open.url("https://www.dr.dk/")

browser.refresh()

#browser.get("https://github.com/jakob-bagterp/")
browser.open.url("https://github.com/jakob-bagterp/")
print(browser.get.text_from_element("/html/body/div[4]/main/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/h1"))
print(browser.get.texts_from_multiple_elements("/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[1]/div/ol/li/div/div/div/div/a"))
print(browser.get.url_from_link("/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[1]/div/ol/li[1]/div/div/div/div/a"))
print(browser.get.urls_from_multiple_links("/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[1]/div/ol/li/div/div/div/div/a"))
xpath = "/html/body/div[4]/main/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/a/img"
browser.wait.for_element(xpath)
print(browser.check_if.is_element_clickable(xpath))
print(browser.check_if.is_element_disabled(xpath))
print(browser.check_if.is_element_enabled(xpath))
print(browser.check_if.is_element_visible(xpath))
print(browser.check_if.is_image_loaded(xpath))
print(browser.get.dimensions_of_element(xpath))

browser.open.url_if_not_current("https://www.dr.dk/")
browser.open.url_if_not_current("https://www.dr.dk/")
browser.open.url_if_not_current("https://www.dr.dk/")
browser.open.url_if_not_current("https://www.dr.dk/")

browser.open.url_in_new_tab("https://github.com/jakob-bagterp/")
print(browser.get.current_url())

time.sleep(5)

#browser.get("https://www.google.dk/")

browser.open.url_if_not_current("https://www.google.dk")

browser.back()
browser.forward()

browser.quit()
