#Class restaurant

class Restaurant():
    """A class that informs if the restaurants is open"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Shows the informations about the restaurant"""
        print(f'The restaurant name is {self.restaurant_name.title()},'
              f'\nand the cuisine type is {self.cuisine_type.title()}.')

    def open_restaurant(self):
        """Shows if the restaurant is open"""
        print(f'The restaurant is open!!')

#Criando instâncias
first_restaurant = Restaurant('Outback', 'Australian food')
second_restaurant = Restaurant('Azzolin', 'Spaghetti')
third_restaurant = Restaurant('dedo de moça', 'Pizza')
#Acessando métodos
first_restaurant.describe_restaurant()
second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()
