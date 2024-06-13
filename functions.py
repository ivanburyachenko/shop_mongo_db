import keyboard
import math
from settings import my_col_p

def catalog_update(list_number):
    products = list(my_col_p.find())
    amount_on_page = 3
    final_page_number = math.ceil(len(products) / amount_on_page)
    sorted_products = []
    for i in range(final_page_number):
        temp = i * amount_on_page
        sorted_products.append(products[temp:temp+amount_on_page]) 
    
    text_for_button_list = []
    for product in sorted_products[list_number]:
        product_id = product["id"]
        product_brand = product["brand"]
        product_name = product["name"]
        product_color = product["color"]
        product_price = product["price"]
        text = f'📦 {product_id}. {product_brand} {product_name} {product_color} - {product_price} грн.'
        text_for_button_list.append(text)

    back_button = True 
    next_button = True

    if list_number == final_page_number-1:   
        next_button = False

    if list_number == 0:
        back_button = False 
    
    result = keyboard.create_catalog(text_for_button_list, back_button, next_button)
    
    return result


