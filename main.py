import csv
import re


def read_file(filename):
    phonebook = []
    with open(filename, "r", newline="", encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            phonebook.append(row)
    return phonebook


def check_fio(name):
    for id, fio in enumerate(all_names):
        if name[0] in fio and name[1] in fio:
            return id
        else:
            return -1


def phone_change(phone):
    pattern = re.compile(r'[+]?[78]?[ ]?[(]?([\d]{3})[)]?[ -]?([\d]{3})[-]?([\d]{2})[-]?'
                         '([\d]{2})([ ]?)[(]?([а-я.]*)[ ]?([\d]*)[)]?')
    phone = pattern.sub(r'+7(\1)\2-\3-\4\5\6\7', phone)
    return phone


def create_newbook(phonebook):
    for person in phonebook:
        name = ' '.join(person[:3]).split()
        if len(name) != 3: name.append(None)
        for i in range (0, 3):
            person[i] = name[i]
        all_names.append((person[:3]))
        person[5] = phone_change(person[5])

    ids = find_id()
    for same_id in ids:
        for id, data in enumerate(zip(phonebook[same_id[0]], phonebook[same_id[1]])):
            if data[0] == '' and data[1] != '':
                phonebook[same_id[0]][id] = phonebook[same_id[1]][id]

    counter = 0
    for id in ids:
        phonebook.pop(id[1] - counter)
        counter += 1

    create_new_file(phonebook)


def find_id():
    same_id = []
    for id, name in enumerate(all_names):
        for i in range (id + 1, len(all_names)):
            if name[0] != all_names[i][0] or name[1] != all_names[i][1]:
                continue
            else:
                same_id.append([id, i])
    return same_id


def create_new_file(list):
    with open('phonebook.csv', 'w', encoding='utf-8-sig', newline='') as file:
        datawriter = csv.writer(file, delimiter=';')
        datawriter.writerows(list)


if __name__ == '__main__':
    all_names = []
    phonebook = read_file("phonebook_raw.csv")
    create_newbook(phonebook)