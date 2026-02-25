import allure

from pages.locators.main_page_locators import OFFICE_DESIGN_SOFTWARE, TOAST_HEADER
from pages.locators.product_page_locators import OFFICE_DESIGN_SOFTWARE_TEXT, ADD_TO_CART_BTN


@allure.feature('Страница товара')
@allure.story('page_url /shop/furn-9999-office-design-software-7')
class TestProductPage:

    @allure.title('Проверка открытия страницы /shop/furn-9999-office-design-software-7?category=9 с главной страницы')
    def test_open_product_page_from_base_page(self, product_page):
        product_page.open_base_page()
        product_page.find_and_click(OFFICE_DESIGN_SOFTWARE)
        product_page.assert_page_url_in_current_url()

    @allure.title('Проверка соответсвия названия продукта')
    def test_checking_product_name(self, product_page, product_name):
        text = product_name
        product_page.open_page_url()
        product = product_page.find(OFFICE_DESIGN_SOFTWARE_TEXT)
        assert product.text == text

    @allure.title('Проверка добавления продукта в корзину')
    def test_add_to_cart(self, product_page, product_name):
        product_page.open_page_url()
        product_page.find_and_click(ADD_TO_CART_BTN)
        assert product_page.find_visible(TOAST_HEADER)
