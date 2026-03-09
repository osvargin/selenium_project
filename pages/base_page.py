import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators.main_page_locators import SHOP_CART, OFFICE_DESIGN_SOFTWARE, TOAST_HEADER
from pages.locators.product_page_locators import OFFICE_DESIGN_SOFTWARE_TEXT


class BasePage:
    base_url = 'http://testshop.qa-practice.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(self.driver)

    @allure.step('Открываем главнцую страницу')
    def open_base_page(self):
        url = self.base_url
        self.driver.get(url)

    @allure.step('Открываем страницу {{page_url}}')
    def open_page_url(self):
        url = f'{self.base_url}{self.page_url}'
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Ищем элемент {locator} и переходим кликом по нему')
    def find_and_click(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator)).click()

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Проверяем, что page_url соответсвует текущему url')
    def assert_page_url_in_current_url(self):
        assert self.page_url in self.driver.current_url

    def presence_of_element_located(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Извлекаем названия товаров')
    def get_product_names(self, locator):
        elements = self.driver.find_elements(*locator)
        return [el.text for el in elements]

    @allure.step('Переходим в корзину товаров')
    def click_shop_cart(self):
        self.find_and_click(SHOP_CART)

    @allure.step('Переходим на страницу товара Office Design Software')
    def click_office_design_software(self):
        self.find_and_click(OFFICE_DESIGN_SOFTWARE)

    @allure.step('Сравниваем отсортированные списки товаров')
    def assert_sorted(self, product_names):
        sorted_names = sorted(product_names)
        assert product_names == sorted_names, 'Товары не отсортированы по названию (A-Z)!'

    @allure.step('Проверяем наличие товаров на странице')
    def assert_len_products(self, products):
        assert len(products) > 0, 'На странице не отображены товары!'

    @allure.step('Проверяем название продукта')
    def assert_product_name(self, text):
        product = self.find(OFFICE_DESIGN_SOFTWARE_TEXT)
        assert product.text == text, 'Названия продуктов отличаются'

    @allure.step('Проверка появления TOAST_HEADER после добавления товара в корзину')
    def assert_toast_header(self):
        self.find_visible(TOAST_HEADER)
