import config1

def print_menu():
    print('Это телефонный справочник. Выберите действие, которое нужно совершить:\n'
          '1. Открыть файл\n'
          '2. Сохранить файл\n'
          '3. Показать контакты\n'
          '4. Добавить контакт\n'
          '5. Изменить контакт\n'
          '6. Найти контакт\n'
          '7. Удалить контакт\n'
          '8. Выход')
    data = int(input('Введите номер необходимого действия: '))
    return data

while True:
    user_choice = print_menu()
    if user_choice == 1:
        print('Открыть файл')
        phone_guide = config1.open_phone_book()
    elif user_choice == 2:
        print('Сохранить файл')
        config1.save_phone_book()
    elif user_choice == 3:
        print('Показать контакты')
        config1.show_contacts()
    elif user_choice == 4:
        print('Добавить контакт')
        config1.add_contact()
    elif user_choice == 5:
        print('Изменить контакт')
        config1.change_contact()
    elif user_choice == 6:
        print('Найти контакт')
        config1.find_contact()
    elif user_choice == 7:
        print('Удалить контакт')
        config1.delete_contact()
    elif user_choice == 8:
        print('Выход')
        config1.quit()
        break

