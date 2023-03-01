from config1 import PhoneBook

pb = PhoneBook('Phone_book.txt')

def print_menu():
    print('''\nЭто телефонный справочник. Возможные действия:
          1. Открыть файл
          2. Сохранить файл
          3. Показать контакт
          4. Добавить контакт
          5. Изменить контакт
          6. Найти контакт
          7. Удалить контакт
          8. Выход''')
    while True:
        choice = input('Введите номер необходимого действия: ')
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        else:
            print('Номер действия должен быть от 1 до 8 включительно. "Давай по новой, Миша.. (с)"')

while True:
    user_choice = print_menu()
    match user_choice:
        case 1:
            print('Открыть файл')
            pb.open_file()
        case 2:
            print('Сохранить файл')
            pb.save_phone_book()
        case 3:
            print('Показать контакты')
            pb.show_contacts()
        case 4:
            print('Добавить контакт')
            pb.add_contact()
        case 5:
            print('Изменить контакт')
            pb.change_contact()
        case 6:
            print('Найти контакт')
            pb.find_contact()
        case 7:
            print('Удалить контакт')
            pb.delete_contact()
        case 8:
            if pb.quit():
                if True:
                    pb.save_phone_book()
            print('До свидания!')
            break

