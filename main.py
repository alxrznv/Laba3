import re


def civil_car_number(string):
    pattern = r'[АВЕКМНОРСТУХавекмнорстух]\d{3}[АВЕКМНОРСТУХавекмнорстух]{2}'
    if re.match(pattern, string):
        return True
    else:
        return False

def military_car_number(string):
    pattern = r'\d{4}[АВЕКМНОРСТУХавекмнорстух]{2}'
    if re.match(pattern, string):
        return True
    else:
        return False

file_path = r'C:\Users\User\PycharmProjects\Laba3\venv\file1'
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        car_number = line.strip()
        if civil_car_number(car_number):
            print(f'"{car_number}" - гражданский автомобильный номер')
        elif military_car_number(car_number):
            print(f'"{car_number}" - военный автомобильный номер')
        else:
            print(f'"{car_number}" - не является автомобильным номером')




print("")
def right_dates(string):
    pattern = r'^20[0-2][0-9]-((0[1-9])|(1[0-2]))-([0-2][1-9]|3[0-1])'
    if re.match(pattern, string):
        return True
    else:
        return False

file_path2 = r'C:\Users\User\PycharmProjects\Laba3\venv\file2'
with open(file_path2, 'r', encoding='utf-8') as file2:
    for line in file2:
        date = line.strip()
        if right_dates(date):
            print(f'"{date}" - верная дата')
        else:
            print(f'"{date}" - неверная дата')