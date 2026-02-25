from selenium.webdriver.common.by import By

PRODUCT_PRICE = (By.CSS_SELECTOR, '[data-oe-expression="product_price"] .oe_currency_value')
TOTAL_UNTAXED = (By.CSS_SELECTOR, '.pb-2 .oe_currency_value')
TOTAL_TAXES = (By.CSS_SELECTOR, '.pb-3 .oe_currency_value')
ORDER_TOTAL = (By.CSS_SELECTOR, '.pt-3 .oe_currency_value')
CHECKOUT_BTN = (By.CSS_SELECTOR, 'a[href="/shop/checkout?express=1"]')
REMOVE_BTN = (By.CSS_SELECTOR, 'a[title="Remove from cart"]')
EMPRY_CART = (By.CSS_SELECTOR, 'js_cart_lines')