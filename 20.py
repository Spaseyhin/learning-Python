

def result(arr):
    
    for i, item in enumerate(arr, 1):
        print(f'{i}. {item}')
    


shoping_list = []
user_input = ""
print("Программа - Записная книга. Введите товар по очереди. Команды: 'Удалить <товар>' - удалить товар, 'Стоп' - завершить программу.")


while user_input != 'Стоп':
    
    user_input = input("Введите команду: ").capitalize()

    print("Программа - Записная книга. Введите товар по очереди. Команды: 'Удалить <товар>' - удалить товар, 'Стоп' - завершить программу.")


    
    if user_input.startswith("Удалить "):
        remove_from_list = user_input[8:].capitalize()  # Извлекаем элемент после "Удалить "
        if shoping_list.count(remove_from_list) == 0:
            print(f'Товара "{remove_from_list}" нет в списке.')
            continue
        shoping_list.remove(remove_from_list)
        print(f'Товар "{remove_from_list}" удален из списка.')
    elif user_input.startswith("Отобразить"):
        print("Список покупок:")

    else:
        if user_input.startswith('Стоп'):

            result(shoping_list)
            break
        add_to_list = user_input 
        shoping_list.append(add_to_list)
        print(f'Товар "{add_to_list}" добавлен в список.')


    result(shoping_list)





