#Class restaurant

class Restaurant():


    def __init__(self, restaurant_name, cuisinte_type):
        self.restaurante_name = restaurant_name
        self.cuisinte_type = cuisinte_type


restaurant = Restaurant("Outback", "Hot")

print(f'{restaurant.restaurante_name}')