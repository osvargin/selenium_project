import allure
from selenium.common import TimeoutException

from pages.base_page import BasePage
from pages.locators.main_page_locators import CONTINUE_SHOPPING_BTN
from pages.locators.shop_cart_locators import CHECKOUT_BTN, REMOVE_BTN


class CartPage(BasePage):
    page_url = '/shop/cart'

    @allure.step('Сравнение цен продукта')
    def assert_price_comparison(self, product_price_locator, total_untaxed_locator, total_tax_locator,
                                order_total_locator):
        product_price = self.find(product_price_locator)
        total_untaxed = self.find(total_untaxed_locator)
        total_taxed = self.find(total_tax_locator)
        order_total = self.find(order_total_locator)
        assert float(product_price.text) == float(total_untaxed.text), 'Цена продукта не равна цене без налога'
        assert float(order_total.text) == float(
            total_untaxed.text) + float(total_taxed.text), ('Конечная цена продукта отличается от суммы цены продукта'
                                                            ' без налога и добавленных налогов')

    @allure.step('Добавляем продукт в корзину')
    def add_to_cart(self, item_locator, cart_locator):
        self.actions.move_to_element(self.find(item_locator)).perform()
        self.find_and_click(cart_locator)
        self.find_and_click(CONTINUE_SHOPPING_BTN)

    @allure.step('Переход по кнопке Checkout')
    def click_checkout(self):
        self.find_and_click(CHECKOUT_BTN)

    @allure.step('Удаляем все товары из корзины')
    def delete_all_products(self):
        buttons = self.find_all(REMOVE_BTN)

        for index, button in enumerate(buttons):
            try:
                with allure.step('Нажимаем кнопку {button}'):
                    self.find_and_click(button)
            except TimeoutException:
                print(f'Таймаут ожидания для кнопки {index + 1}. Пропускаем.')
            except Exception as e:
                print(f'Ошибка при клике на кнопку {index + 1}: {e}')
