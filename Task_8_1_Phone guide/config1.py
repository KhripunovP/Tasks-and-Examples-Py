import re
phone_guide = []

def open_phone_book():
    with open('Phone_book.txt', 'r', encoding = 'utf-8') as data:
        phone_guide = data.readlines()
        print('Файл открыт')
        return phone_guide

def save_phone_book():
    with open('Phone_book.txt', 'w', encoding = 'utf-8') as data:
        for i in phone_guide:
            data.write(i)

def show_contacts():
    if(len(phone_guide)) == 0:
        print('Файл не открыт либо пуст')
    else:
        for i in phone_guide:
            print(' '.join(i.split(';')))

def add_contact():
    if(len(phone_guide)) == 0:
        print('Файл не открыт либо пуст')
    else:
        user_info = input('Введите данные нового контакта:')
        user_info = ';'.join(user_info.split(' '))
        phone_guide.append('\n' + user_info)

def change_contact():
    if(len(phone_guide)) == 0:
        print('Файл не открыт либо пуст')
    else:
        user_info = input('Введите имя или номер контакта, который Вы хотите изменить: ')
        new_user_info = input(str('Введите новый номер контакта: '))
        for i in range(len(phone_guide)):
            search = re.findall(user_info, phone_guide[i], re.IGNORECASE)
            if len(search) != 0:
                phone_guide[i] = re.sub('\d+', new_user_info, phone_guide[i]) #Замена всех цифр строки на новые цифры
                print(phone_guide[i])
                break
            if (i == len(phone_guide) - 1) and (len(search) == 0):
                print('Такого контакта нет')

def find_contact():
    if(len(phone_guide)) == 0:
        print('Файл не открыт либо пуст')
    else:
        user_info = input('Введите имя или номер контакта, который необходимо найти: ')
        for i in range(len(phone_guide)):
            search = re.findall(user_info, phone_guide[i], re.IGNORECASE)
            if len(search) != 0:
                print(phone_guide[i])
                break
            if (i == len(phone_guide) - 1) and (len(search) == 0):
                print('Такого контакта нет')

def delete_contact():
    if (len(phone_guide)) == 0:
        print('Файл не открыт либо пуст')
    else:
        user_info = input('Введите имя или номер контакта, который необходимо удалить: ')
        for i in range(len(phone_guide)):
            search = re.findall(user_info, phone_guide[i], re.IGNORECASE)
            if len(search) != 0:
                print(phone_guide[i])
                decision = input('Точно удаляем контакт? y - да, n - нет: ')
                if decision == 'Y' or 'y':
                    phone_guide.pop(i)
                else:
                    print('Удаление отменено')
                break
            if (i == len(phone_guide) - 1) and (len(search) == 0):
                print('Такого контакта нет')

def quit():
    with open('Phone_book.txt', 'r', encoding = 'utf-8') as data:
        data.close()

phone_guide = open_phone_book()
