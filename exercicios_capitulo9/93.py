# User profile

class User:
    def __init__(self, first_name, last_name, age, country, city):
        """User data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age =age
        self.country = country
        self.city = city

    def describe_user(self):
        """Data user resume"""
        data = {'first_name': self.first_name, 'last_name': self.last_name,
                'age': str(self.age), 'country': self.country, 'city': self.city}
        print(f'{data}')
    def great_user(self):
        """personalized greeting"""
        print(f'Hello, {self.first_name} {self.last_name}!')


#Criando instâncias
first_user = User('Douglas', 'Cortez', 26, 'Brazil', 'Vinhedo')
second_user = User('Sabrina', 'Zanardi', 25, 'Brazil', 'Vinhedo')
#Chamando os métodos
first_user.describe_user()
first_user.great_user()
second_user.describe_user()
second_user.great_user()
