"""CP1404 shopping console program"""
import json
from product import Product


def main():
    """Simple program to load and display products."""
    filename = "products.json"
    products = load_products(filename)
    print(f"{len(products)} products loaded from {filename}")
    for product in products:
        print(product)


def load_products(filename):
    """Load products from filename"""
    products = []
    with open(filename) as in_file:
        records = json.load(in_file)
    print(repr(records))  # Let's see what the data looks like
    for record in records:
        products.append(Product(**record))
    return products


if __name__ == '__main__':
    main()
