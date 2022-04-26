car_prices = {'opel': 5000, 'toyota': 7000, 'bmw': 10000}
print(car_prices)
print(car_prices['toyota'])

car_prices['mazda'] = 2000
print(car_prices)

del car_prices['mazda']
print(car_prices)

car_prices.clear()
print(car_prices)

person = {
    'first name': 'Jack',
    'last name': 'Gobkov',
    'age': 27,
    'hobbies': ['football', 'programming'],
    'children': {'son' : 'Denys', 'daughter': 'Alina'}
}

print(person)
print(person['age'])

hobbies = person['hobbies']
print(hobbies[1])

