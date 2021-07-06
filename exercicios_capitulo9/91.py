#Class restaurant

class Restaurant():
    """A class that informs if the restaurants is open"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Shows the informations about the restaurant"""
        print(f'The restaurant name is {self.restaurant_name.title()}.'
              f'\nand the cuisine type is {self.cuisine_type.title()}.')

    def open_restaurant(self):
        """Shows if the restaurant is open"""
        print(f'The restaurant is open!!')

#Criando uma instância
first_restaurant = Restaurant('Outback', 'Australian food')
#Acessando atributos
print(f'The restaurant name is {first_restaurant.restaurant_name.title()}.')
print(f'The cuisine type is {first_restaurant.cuisine_type.title()}')
#Acessando métodos
first_restaurant.describe_restaurant()
first_restaurant.open_restaurant()
