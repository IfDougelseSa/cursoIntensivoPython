# Informations about a car

def make_car(manufacturer_name, car_model, **informations):
    """Shows the information about a car"""
    car = {}
    car['manufacture'] = manufacturer_name
    car['model'] = car_model
    for key, values in informations.items():
        car[key] = values
    return car

car = make_car('subaro', 'outback', color='blue', tow_package=True)
print(car)
