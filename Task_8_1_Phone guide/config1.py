import re
from copy import deepcopy

phone_guide = []
path = 'Phone_book.txt'
new_phone_guide = []

def open_phone_book():
    global phone_guide
    global new_phone_guide
    global path
    with open(path, 'r', encoding = 'utf-8') as file:
        data = file.readlines()
        for contact in data:
            phone_guide.append(contact)
        print('Файл открыт')
    new_phone_guide = deepcopy(phone_guide)

def save_phone_book():
    global phone_guide
    global path
    with open(path, 'w', encoding = 'utf-8') as file:
        for i in phone_guide:
            file.write(i)

def show_contacts():
    global phone_guide
    if(len(phone_guide)) == 0:
        print('Файл не открыт либо пуст')
    else:
        for i in phone_guide:
            print(' '.join(i.split(';')))

def add_contact():
    global phone_guide
    if(len(phone_guide)) == 0:
        print('Файл не открыт либо пуст')
    else:
        user_info = input('Введите данные нового контакта:')
        user_info = ';'.join(user_info.split(' '))
        phone_guide.append('\n' + user_info)

def change_contact():
    global phone_guide
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
    global phone_guide
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
    global phone_guide
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
    global phone_guide
    global new_phone_guide
    print(phone_guide)
    print(new_phone_guide)

    if phone_guide != new_phone_guide:
        answer = input('У вас есть несохраненные изменения, хотите их сохранить? (y/n)')
        return True if answer == 'y' else False

