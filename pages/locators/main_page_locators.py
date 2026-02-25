from selenium.webdriver.common.by import By

SHOP_CART = (By.CSS_SELECTOR, 'a[href="/shop/cart"]')
CUSTOMIZABLE_DESK = (By.CSS_SELECTOR, 'a[content="Customizable Desk"]')
CART_BTN_FOR_CUSTOMIZABLE_DESK = (By.CSS_SELECTOR, '[value="12"] + [role="button"]')
CONTINUE_SHOPPING_BTN = (By.CSS_SELECTOR, '.btn-secondary')
TOAST_HEADER = (By.CSS_SELECTOR, '.toast-header')
CATEGORIES_BTN = (By.CSS_SELECTOR, '#top_menu > li > a')
DESKS_BTN = (By.CSS_SELECTOR, '#top_menu > li > ul > li:nth-child(1) > a')
OFFICE_DESIGN_SOFTWARE = (By.CSS_SELECTOR, 'a[content="Office Design Software"]')
