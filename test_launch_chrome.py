import time
from src.browserist import Browser

browser = Browser()

browser.open.url("https://www.dr.dk/")
print("page_title", browser.get.page_title())
browser.refresh()
browser.scroll.into_view("//footer")
browser.scroll.into_view_if_not_visible("//footer")
browser.scroll.into_view_if_not_visible("/html/body/div[2]/div/div[3]/div/main/div[1]/div/div/section/div[2]/div/div/ul")

browser.open.url_if_not_current("https://github.com/jakob-bagterp/browserist")
for i in range(2, 9):
    browser.hover.mouse_on_element(f"//*[@id='repo-content-pjax-container']/div/div[3]/div[1]/div[2]/div[3]/div[1]/div[{i}]")

browser.open.url("https://github.com/jakob-bagterp/")
browser.wait.until_url_contains("jakob")
browser.scroll.to_end_of_page()
browser.scroll.to_position(100, 100)
browser.scroll.to_top_of_page()
browser.wait.until_url_is(browser.get.url.current())
print(browser.get.text.from_element("/html/body/div[4]/main/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/h1"))
print(browser.get.text.from_multiple_elements("/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[1]/div/ol/li/div/div/div/div/a"))
print(browser.get.url.from_link("/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[1]/div/ol/li[1]/div/div/div/div/a"))
multiple_links_xpath = "/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[1]/div/ol/li/div/div/div/div/a"
print(browser.get.url.from_multiple_links(multiple_links_xpath))
print("count_elements", browser.tools.count_elements(multiple_links_xpath))
print("attribute.value_from_multiple_elements", browser.get.attribute.value_from_multiple_elements(multiple_links_xpath, "href"))
xpath = "/html/body/div[4]/main/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/a/img"
browser.wait.for_element(xpath)
browser.wait.until_element_disappears(xpath + "/test")
browser.wait.until_images_have_loaded(xpath)
browser.wait.until_page_title_contains(browser.get.page_title())
browser.wait.until_page_title_is(browser.get.page_title())
print("page_title", browser.get.page_title())
print("does_element_exist", browser.check_if.does_element_exist(xpath))
print("is_element_clickable", browser.check_if.is_element_clickable(xpath))
print("is_element_disabled", browser.check_if.is_element_disabled(xpath))
print("is_element_enabled", browser.check_if.is_element_enabled(xpath))
print("is_element_visible", browser.check_if.is_element_visible(xpath))
print("is_image_loaded", browser.check_if.is_image_loaded(xpath))
print("dimensions_of_element", browser.get.dimensions_of_element(xpath))
print("is_url_valid", browser.tools.is_url_valid(browser.get.url.current()))
print("is_input_valid", browser.tools.is_input_valid(xpath, xpath + "test"))
print("url_from_image", browser.get.url.from_image(xpath))
print("url_from_multiple_images", browser.get.url.from_multiple_images(xpath))
print("attribute_value", browser.get.attribute.value(xpath, "src"))
search_field_xpath = "/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]"
browser.select.input_field(search_field_xpath)
browser.wait.random_time(3, 5)
browser.click.button_if_contains_text("/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[1]/div/ol/li[1]/div/div/div/div/a", "browserist", ignore_case = True)
time.sleep(3)

browser.open.url_if_not_current("https://www.dr.dk/")
browser.open.url_if_not_current("https://www.dr.dk/")
browser.open.url_if_not_current("https://www.dr.dk/")

browser.open.url_if_not_current("https://www.google.dk")

browser.back()
browser.forward()

browser.quit()
