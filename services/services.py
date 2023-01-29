from database.database import products_category, user_db
from products_data.products_data import products_data

products = products_data['products']


def get_products_by_category(callback_category: str, _id):
    num = ""
    for c in callback_category:
        if c.isdigit():
            num += c

    res = []
    for product in products:
        if product['category'] in products_category.get(num):
            res.append(product)
    user_db[_id]['watching']['products_count'] = len(res)
    user_db[_id]['watching']['products'] = res


def generate_product_info(product: dict):
    return f'<b>Артикул:</b> <pre>{product["item"]}</pre>\n' \
           f'<b>Цена:</b> {product["price"]} ₸\n' \
           f'<ins>{product["availability"]}</ins>\n' \
           f'<b>Описание:</b> {product["title"]}\n'


def get_bookmarks(_id):
    return user_db[_id]['bookmarks']
