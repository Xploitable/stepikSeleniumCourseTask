import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_cart_button(browser):
    browser.get(link)
    browser.find_element_by_class_name("btn-add-to-basket")
    #time.sleep(30) # для визуальной проверки языка страницы и кнопки
    