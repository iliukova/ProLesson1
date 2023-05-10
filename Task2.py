# Необхідно розробити Python-скрипт, який буде повертати користувачеві меню ресторану.
# Зазвичай, меню ресторану містить наступні елементи:
# - Категорії страв (наприклад, закуски, основні страви, десерти).
# - Страви у кожній категорії. Основні класи, які необхідно створити для реалізації меню ресторану:
# Клас Страва: відповідає за збереження інформації про окрему страву, включаючи її назву, опис та ціну.
# Клас Категорія страв: відповідає за збереження страв, які належать до конкретної категорії.
# Включає список об'єктів "Страва". Клас Меню: відповідає за збереження всіх категорій страв
# та їхнього вмісту. Включає список об'єктів "Категорія страв".
# Клас Замовлення: відповідає за збереження списку страв, які замовив клієнт, та їхньої ціни.

class Dish:
    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f'{self.name}: {self.price:.2f}'

class MenuCategory:
    def __init__(self, name):
        self.name = name
        self.dishes = []

    def add_dishes(self, name, dishes):
        self.name=name
        self.dishes.append(dishes)

menucategory1 = MenuCategory("Салат")
menucategory1.dishes.append("САЛАТ З СИРОМ ФЕТА ТА БУРЯКОМ")
menucategory1.dishes.append("ЦЕЗАР З КУРКОЮ")
menucategory1.dishes.append("КАПРЕЗЕ")
print(menucategory1)
class Menu:
    def __init__(self, categories):
        self.categories = categories

class Order:
    def __init__(self):
        self.dishes = []
        self.quantities = []

    def add_dish(self, dish, quantity=1):
        self.dishes.append(dish)
        self.quantities.append(quantity)

    def __str__(self):
        res = ''
        for dishes, quantity in zip(self.dishes, self.quantities):
            res += f'{dishes} x {quantity} = {dishes.price * quantity} грн\n'
        return res

order = Order()
d_1 = Dish('САЛАТ З СИРОМ ФЕТА ТА БУРЯКОМ', "Буряк, сир Фета, листя салатів Рукола, Айсберг, Шпинат, чорнослив, яблука, грецькі горіхи, соус Вінегрет", 135)
d_2 = Dish('ЦЕЗАР З КУРКОЮ', "Курка в соусі Теріякі, салат Ромен, сир Пармезан, бекон, помідори Чері, перепелині яйця, грінки з багету, соус Цезар",  220)
d_3 = Dish('КАПРЕЗЕ', "Сир Моцарела, помідори, салат Рукола, соус Песто, цитрусова заправка", 210)

order.add_dish(d_1)
order.add_dish(d_2, 3)
order.add_dish(d_3, 2)

print(order)