import allure

from pages.locators.main_page_locators import CATEGORIES_BTN, DESKS_BTN
from pages.locators.desk_page_locators import PRODUCT_CONTAINER, PRODUCT_CARD, SORT_BY_BTN, SORT_BY_NAME


@allure.feature('Категория столы')
@allure.story('page_url /shop/category/desks-1')
class TestDeskPage:

    @allure.title('Проверка открытия страницы /shop/category/desks-1 с главной страницы')
    def test_open_desk_page_from_base_page(self, desk_page):
        desk_page.open_base_page()
        desk_page.go_to_desk_page(CATEGORIES_BTN, DESKS_BTN)
        desk_page.assert_page_url_in_current_url()

    @allure.title('Проверка наличия товаров')
    def test_page_loads_and_products_displayed(self, desk_page):
        desk_page.open_page_url()
        products = desk_page.wait_for_products_loaded(PRODUCT_CONTAINER, PRODUCT_CARD)
        assert len(products) > 0, 'На странице не отображены товары!'

    @allure.title('Проверка сортировки товаров')
    def test_products_sorted_by_name_ascending(self, desk_page):
        desk_page.open_page_url()
        desk_page.sorted(SORT_BY_BTN, SORT_BY_NAME)
        product_names = desk_page.products_name_from_page(PRODUCT_CONTAINER, PRODUCT_CARD)
        sorted_names = sorted(product_names)
        assert product_names == sorted_names, 'Товары не отсортированы по названию (A-Z)!'
