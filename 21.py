menu = ('sushi', 'pizza','burger')

print(menu[1])

shushi, pizza, burger = menu
print(shushi)
print(pizza)
print(burger)


def get_name_age():
    name = input('Введите имя: ')
    age = input('Введите возраст: ')

    return (name,age)


alex, old = get_name_age()

print(f'Имя: {alex}, Возраст: {old}')


products = [
    ('яблоко', 50),
    ('банан', 30),
    ('киви', 70),
    ('арбуз', 100)
    ]

for product, price in products:
    print(f'Продукт: {product}, Цена: {price}')



def get_user_info(name):
    all_names = [('Саша', 25, 'Саратов'), ('Лари', 30, 'Москва'), ('Маша', 22,'Казань')]
    for  person in  all_names:
        if person[0] == name:
            return person
            
    
    return(None, None, None)


user_input = input('Введите имя: ')

found_name, age, city = get_user_info(user_input)
print(f'Имя: {found_name}, Возраст: {age}, Город: {city}')
