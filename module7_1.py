class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        info = file.read()
        file.close()
        return info

    def add(self, *products):
        for i in products:
            product = str(i)
            # if product.split(',')[0] in self.get_products():      # условие если всё-таки проверка идёт по названию
            #     print(f'Продукт {product} уже есть в магазине')
            if product in self.get_products():                      # условие для выполнения программы как в примере
                print(f'Продукт {product} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{product}\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
