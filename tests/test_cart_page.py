import allure

from pages.locators.main_page_locators import SHOP_CART
from pages.locators.shop_cart_locators import PRODUCT_PRICE, TOTAL_UNTAXED, TOTAL_TAXES, ORDER_TOTAL


@allure.feature('Корзина')
@allure.story('page_url /shop/cart')
class TestCartPage:

    @allure.title('Проверка открытия корзины с главной страницы')
    def test_open_cart_from_base_page(self, base_page, cart_page):
        base_page.open_base_page()
        base_page.find_and_click(SHOP_CART)
        cart_page.assert_page_url_in_current_url()

    @allure.title('Проверка корректности вычисления суммы Total')
    def test_total_sum(self, base_page, cart_page, add_and_delete_product):
        base_page.find_and_click(SHOP_CART)
        cart_page.assert_price_comparison(PRODUCT_PRICE, TOTAL_UNTAXED, TOTAL_TAXES, ORDER_TOTAL)

    @allure.title('Проверка перехода по кнопке Checkout')
    def test_checkout(self, base_page, cart_page, shipping_page, add_product_to_cart):
        base_page.find_and_click(SHOP_CART)
        cart_page.click_checkout()
        shipping_page.assert_page_url_in_current_url()
