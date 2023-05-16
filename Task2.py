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
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price} uah'


class Category:
    def __init__(self, title):
        self.title = title
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def __str__(self):
        return f"{'*' * 10}{self.title}{'*' * 10}\n" + '\n'.join(map(str, self.dishes))


class Menu:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def __str__(self):
        return '\n'.join(map(str, self.categories))


dish_1 = Dish('Страва 1', 100)
dish_2 = Dish('Страва 2', 101)
dish_3 = Dish('Страва 3', 102)
dish_4 = Dish('Страва 4', 103)
dish_5 = Dish('Страва 5', 104)
dish_6 = Dish('Страва 6', 105)
dish_7 = Dish('Страва 7', 106)
dish_8 = Dish('Страва 8', 107)
dish_9 = Dish('Страва 9', 108)
dish_10 = Dish('Страва 10', 109)

cat_1 = Category('Основні страви')
cat_1.add_dish(dish_1)
cat_1.add_dish(dish_2)
cat_1.add_dish(dish_3)
cat_1.add_dish(dish_4)
cat_1.add_dish(dish_5)

cat_2 = Category('Перші страви')
cat_2.add_dish(dish_6)
cat_2.add_dish(dish_7)
cat_2.add_dish(dish_8)
cat_2.add_dish(dish_9)
cat_2.add_dish(dish_10)

menu = Menu()
menu.add_category(cat_1)
menu.add_category(cat_2)

print(menu)
