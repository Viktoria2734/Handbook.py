def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')


def email_is_valid():
    return True


class Directory:
    handbook = {}

    # ['email'] = ['имя','фамилия','телефон','город']

    def add_note(self, email, name, surname, phone_number, city):
        if email not in self.handbook.keys():
            if email_is_valid:
                self.handbook[email] = [name, surname, phone_number, city]

    def find_note(self, email):
        if email in self.handbook.keys():
            return self.handbook[email]
        return

    def change_note(self, email, name, surname, phone_number, city):
        if email not in self.handbook.keys():
            return
        if len(str(name)):
            self.handbook[email][0] = name
        if len(str(surname)):
            self.handbook[email][1] = surname
        if len(str(phone_number)):
            self.handbook[email][2] = phone_number
        if len(str(city)):
            self.handbook[email][3] = city

    def delete_note(self, email):
        if email in self.handbook.keys():
            self.handbook.pop(email)
        return


directory = Directory()

directory.add_note('belovdima@gmail.com', 'Дмитрий', 'Белов', '89686070901', 'Москва')
directory.add_note('ivkolesnikov@mail.ru', 'Иван', 'Колесников', '89191200447', 'Магнитогорск')
directory.add_note('valeriasmirnova@gmail.com', 'Валерия', 'Смирнова', '89044972586', 'Тюмень')
print(directory.handbook)

directory.change_note('valeriasmirnova@gmail.com', '', 'Зотова', '', '')
directory.change_note('ivkolesnikov@mail.ru', '', '', '89514492307', '')
print(directory.handbook)

print(directory.find_note('belovdima@gmail.com'))
print(directory.find_note('ivkolesnikov@mail.ru'))
print(directory.find_note('qabc@mail.com'))

directory.delete_note('belovdima@gmail.com')
print(directory.handbook)
