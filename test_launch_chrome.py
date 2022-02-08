import time
from src.browserist import Browser

browser = Browser()

browser.open.url("https://www.dr.dk/")
print("current_page_title", browser.get.current_page_title())
browser.refresh()

#browser.get("https://github.com/jakob-bagterp/")
browser.open.url("https://github.com/jakob-bagterp/")
browser.wait.until_url_contains("jakob")
print(browser.get.text_from_element("/html/body/div[4]/main/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/h1"))
print(browser.get.texts_from_multiple_elements("/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[1]/div/ol/li/div/div/div/div/a"))
print(browser.get.url_from_link("/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[1]/div/ol/li[1]/div/div/div/div/a"))
multiple_links_xpath = "/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[1]/div/ol/li/div/div/div/div/a"
print(browser.get.urls_from_multiple_links(multiple_links_xpath))
print("count_number_of_elements", browser.tools.count_number_of_elements(multiple_links_xpath))
xpath = "/html/body/div[4]/main/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/a/img"
browser.wait.for_element(xpath)
browser.wait.until_element_disappears(xpath + "/test")
browser.wait.until_images_have_loaded(xpath)
browser.wait.until_page_title_contains(browser.get.current_page_title())
browser.wait.until_page_title_is(browser.get.current_page_title())
print("current_page_title", browser.get.current_page_title())
print("does_element_exist", browser.check_if.does_element_exist(xpath))
print("is_element_clickable", browser.check_if.is_element_clickable(xpath))
print("is_element_disabled", browser.check_if.is_element_disabled(xpath))
print("is_element_enabled", browser.check_if.is_element_enabled(xpath))
print("is_element_visible", browser.check_if.is_element_visible(xpath))
print("is_image_loaded", browser.check_if.is_image_loaded(xpath))
print("dimensions_of_element", browser.get.dimensions_of_element(xpath))
print(browser.get.url_from_image(xpath))
print(browser.get.urls_from_multiple_images(xpath))

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
