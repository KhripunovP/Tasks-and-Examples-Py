import re
from copy import deepcopy

class PhoneBook:
    path = 'Phone_book.txt'

    def __init__(self, path):
        self.path = path
        self.phone_guide = []
        self.old_phone_guide = []

    def open_file(self):
        with open(self.path, 'r', encoding = 'utf-8') as file:
            data = file.readlines()
            for contact in data:
                self.phone_guide.append(contact.strip()) # strip убирает лишние пробелы типа \n - лишний перенос строки
            print('Файл открыт')
        self.old_phone_guide = deepcopy(self.phone_guide)

    def save_phone_book(self):
        with open(self.path, 'w', encoding = 'utf-8') as file:
            for i in self.phone_guide:
                file.write(i)

    def show_contacts(self):
        if(len(self.phone_guide)) == 0:
            print('Файл не открыт либо пуст')
        else:
            for i in self.phone_guide:
                print(' '.join(i.split(';')))

    def add_contact(self):
        if(len(self.phone_guide)) == 0:
            print('Файл не открыт либо пуст')
        else:
            user_info = input('Введите данные нового контакта:')
            user_info = ';'.join(user_info.split(' '))
            self.phone_guide.append('\n' + user_info)

    def change_contact(self):
        if(len(self.phone_guide)) == 0:
            print('Файл не открыт либо пуст')
        else:
            user_info = input('Введите имя или номер контакта, который Вы хотите изменить: ')

            for i in range(len(self.phone_guide)):
                search = re.findall(user_info, self.phone_guide[i], re.IGNORECASE)
                if len(search) != 0:
                    print (self.phone_guide[i])
                    question = input ('Этот номер хотите изменить? (y/n)')
                    if question == 'y':
                        new_user_info = input(str('Введите новый номер контакта: '))
                        self.phone_guide[i] = re.sub('\d+', new_user_info, self.phone_guide[i]) #Замена всех цифр строки на новые цифры
                        print(self.phone_guide[i])
                        break
                    if (i == len(self.phone_guide) - 1) and (len(search) == 0):
                        print('Такого контакта нет')

    def find_contact(self):
        search_result = []
        if(len(self.phone_guide)) == 0:
            print('Файл не открыт либо пуст')
        else:
            user_info = input('Введите имя или номер контакта, который необходимо найти: ')
            for i in range(len(self.phone_guide)):
                search = re.findall(user_info, self.phone_guide[i], re.IGNORECASE)
                if len(search) != 0:
                    search_result.append(self.phone_guide[i])
                if (i == len(self.phone_guide) - 1) and (len(search_result) == 0):
                    print('Такого контакта нет')
        for i in search_result:
            print(' '.join(i.split(';')))

    def delete_contact(self):
        search_result = []
        if (len(self.phone_guide)) == 0:
            print('Файл не открыт либо пуст')
        else:
            user_info = input('Введите имя или номер контакта, который необходимо удалить: ')
            for i in range(len(self.phone_guide)):
                search = re.findall(user_info, self.phone_guide[i], re.IGNORECASE)
                if len(search) != 0:
                    search_result.append(self.phone_guide[i])
                if (i == len(self.phone_guide) - 1) and (len(search) == 0):
                    print('Такого контакта нет')
            if len(search_result) != 0:
                for i, item in enumerate(search_result, 1):
                    print(f'{i}. {item}')
                decision = int(input('укажите номер контакта в результате поиска, который хотите удалить:'))
                print(search_result[decision - 1])
                for i in range(len(self.phone_guide)):
                    if self.phone_guide[i] == search_result[decision - 1]:
                        self.phone_guide.pop(i)
                        print('Контакт удален')
                        break

    def quit(self):
        if self.phone_guide != self.old_phone_guide:
            answer = input('У вас есть несохраненные изменения, хотите их сохранить? (y/n)')
            return True if answer == 'y' else False

