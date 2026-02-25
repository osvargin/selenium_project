import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.desk_page import DeskPage
from pages.locators.main_page_locators import CUSTOMIZABLE_DESK, CART_BTN_FOR_CUSTOMIZABLE_DESK, TOAST_HEADER, \
    OFFICE_DESIGN_SOFTWARE
from pages.locators.product_page_locators import OFFICE_DESIGN_SOFTWARE_TEXT
from pages.locators.shipping_page_locators import ShippingPage
from pages.locators.shop_cart_locators import EMPRY_CART
from pages.product_page import ProductPage


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture
def actions(driver):
    return ActionChains(driver)


@pytest.fixture
def base_page(driver):
    return BasePage(driver)


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture
def shipping_page(driver):
    return ShippingPage(driver)


@pytest.fixture
def add_product_to_cart(driver, base_page, cart_page):
    base_page.open_base_page()
    cart_page.add_to_cart(CUSTOMIZABLE_DESK, CART_BTN_FOR_CUSTOMIZABLE_DESK)
    base_page.find_visible(TOAST_HEADER)


@pytest.fixture
def del_all_product_at_cart(driver, base_page, cart_page):
    cart_page.delete_all_products()
    base_page.find_visible(EMPRY_CART)


@pytest.fixture
def add_and_delete_product(driver, add_product_to_cart, cart_page):
    yield
    cart_page.delete_all_products()


@pytest.fixture
def desk_page(driver):
    return DeskPage(driver)


@pytest.fixture
def product_page(driver):
    return ProductPage(driver)


@pytest.fixture
def product_name(product_page):
    product_page.open_base_page()
    product = product_page.find(OFFICE_DESIGN_SOFTWARE)
    return product.text
