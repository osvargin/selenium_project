import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    @allure.step('Получаем список товаров')
    def wait_for_products_loaded(self, container_locator, locator):
        self.find_visible(container_locator)
        products = self.find_all(locator)
        return products

    @allure.step('Извлекаем названия товаров')
    def get_product_names(self, locator):
        elements = self.driver.find_elements(*locator)
        return [el.text for el in elements]
