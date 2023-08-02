from project.drink import Drink
from project.food import Food
from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        product = [x for x in self.products if x.name == product_name][0]
        if product:
            return product

    def remove(self, product_name):
        product = [x for x in self.products if x.name == product_name]
        if product:
            self.products.remove(product[0])

    def __repr__(self):
        result = []
        for product in self.products:
            result.append(f'{product.name}: {product.quantity}')
        nl = '\n'
        return f'{nl.join(result)}'
