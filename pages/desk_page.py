import re

import allure

from pages.base_page import BasePage


class DeskPage(BasePage):
    page_url = '/shop/category/desks-1'

    @allure.step('Переходим на страницу /shop/category/desks-1')
    def go_to_desk_page(self, category_locator, desk_locator):
        with allure.step(f'Наводимся на элемент {category_locator}'):
            self.actions.move_to_element(self.find(category_locator)).perform()
            self.find_and_click(desk_locator)

    @allure.step('Выбираем сортировку в списке')
    def sorted(self, locator, sort_option_text):
        self.find_and_click(locator)
        self.find_and_click(sort_option_text)

    @allure.step('Собираем список товаров со страницы')
    def products_name_from_page(self, container_locator, product_locator):
        product_elements = self.wait_for_products_loaded(container_locator, product_locator)
        product_names = [
            re.sub(r'\s*\$\s*[\d,]+\.?\d*\s*$', '',
                   re.sub(r'\s+', ' ', element.text.strip()).lower())
            for element in product_elements
            if element.text and element.text.strip()
        ]
        return product_names
