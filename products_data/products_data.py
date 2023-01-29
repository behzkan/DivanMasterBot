import json


products_data = {
    'products': [],
    'size': 0
}


def load_products(path):
    with open(path, encoding='utf8') as f:
        products_dict: dict = json.load(f)
    products_data['size'] = len(products_dict)
    for value in products_dict.values():
        products_data['products'].append(value)
# load_products('products.json')
