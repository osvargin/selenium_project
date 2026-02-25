from selenium.webdriver.common.by import By

PRODUCT_CARD = (By.CSS_SELECTOR, '.oe_product')
NAME_PRODUCT_CARD = (By.CSS_SELECTOR, '.text-primary')
PRODUCT_CONTAINER = (By.CSS_SELECTOR, '#products_grid')
SORT_BY_BTN = (By.CSS_SELECTOR, '.o_sortby_dropdown [role="button"]')
SORT_BY_NAME = (By.LINK_TEXT, 'Name (A-Z)')
