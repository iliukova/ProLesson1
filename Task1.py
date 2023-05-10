# Створіть клас Product для опису товару. У якості атрибутів товару можна використовувати назву, цінц та опис товару. Створіть декілька інстансів класу Product.
# Створіть клас Cart, який буде виступати у якості кошика з товарами певного покупця. Кошик може містити декілька товарів певної кількості. Реалізуйте метод обчислення вартості кошика.
# В усіх класах має бути визначений метод str.
class Product:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}: {self.price:.2f}'


class Cart:

    def __init__(self):
        self.products = []
        self.quantities = []

    def add_product(self, product, quantity=1):
        self.products.append(product)
        self.quantities.append(quantity)

    def __str__(self):
        res = ''
        for product, quantity in zip(self.products, self.quantities):
            res += f'{product} x {quantity} = {product.price * quantity} грн\n'
        return res


cart = Cart()
pr_1 = Product('banana', 60)
pr_2 = Product('apple', 61)
pr_3 = Product('orange', 62)

cart.add_product(pr_1)
cart.add_product(pr_2, 3)
cart.add_product(pr_3, 2)

print(cart)
