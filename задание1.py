# Псевдо код:

# Для каждого файла 
#     Для каждого имени в файле
#         Взять последную букву из имени
#         Взять число людей с этим именем
#         Добавить букву в словарь как ключь
#         Для ключа Увеличить количество мальчиков или девочек на число 

# Формат данных:
# ID;Name;NumberOfPersons;global_id;Year;Month
# 1;Александр;253;37750243;2015;январь

# Словарь:
#     буква: (кол-во М, кол-во Ж)

def main():
    # Лист файлов с именами. Каждый элемент в списке содержит кортеж 
    files = [
        ('./Boys.csv','М'),
        ('./Girls.csv','Ж'),
    ]
    # Статистика букв в форме словаря. 
    analiz = {}
    # Сколько букв в имени считать
    kol_bukv = 1


    print('... Анализ данных ...')
    for ftuple in files: # В каждом файле
        with open(ftuple[0], encoding='cp1251') as f:
            f.readline() 
            for line in f.readlines(): # Для каждого имени

                data = line.split(';') # Делим каждую строку по символу ;
                name = data[1] # Имя
                number = int(data[2]) # data[2] , согласно с форматом вводных файлов CSV это столбец NumberOfPersons. То есть кол-во людей с этим именем в данном месяце
                bukva = name.strip()[-kol_bukv:] # Берем нужное число букв с конца имени

                # Сохраняем результаты в словарь.
                if analiz.get(bukva) is None:                   # такой буквы еще не было
                    if ftuple[1] == 'М': # Если пол файла М
                        # Здесь и ниже. Первое число мальчики, второе девочки
                        analiz[bukva] = (number, 0)
                    else: # Если пол Ж
                        analiz[bukva] = (0, number)
                else:                                           # такая буква уже была, нужно прибавить к тому что уже есть
                    if ftuple[1] == 'М': # Если пол файла М
                        analiz[bukva] = (analiz.get(bukva)[0] + number, analiz.get(bukva)[1])
                    else:
                        analiz[bukva] = (analiz.get(bukva)[0], analiz.get(bukva)[1] + number)

    print('Таблица результатов')
    # Здесь и далее  :^10 - делает минимальный размер ячейки в таблице, что бы было красиво. 
    tabl = '|{:^10}|{:^10}|{:^10}|{:^10}|'.format('Letter', '% Male', '% Female', 'Total')
    print(tabl)
    print('-' * len(tabl))
    # Можно сортировать словарь по алфавиту с функцией sorted()
    for key, value in analiz.items():
        total = int(value[0]) + int(value[1])
        males = value[0]/total * 100
        females = value[1]/total * 100
        # .2f округлит процент до двух чисел после запятой
        print('|{:^10}|{:^10.2f}|{:^10.2f}|{:^10}|'.format(key,males,females,total))
    
    # Фунция для где пользователь може ввести имя
    user_input(analiz, kol_bukv)
    
def user_input(analiz, kb):

    while(True):
        name = input('Имя? ')
        bukva = name[-kb:]
        if analiz.get(bukva) is None:
            print('Нет данных для букв(ы) {}. Может еще разок?'.format(bukva))
        else:
            value = analiz.get(bukva)
            total = int(value[0]) + int(value[1])
            male = value[0]/total * 100
            female = value[1]/total * 100
            greeting = ''
            if female > male:
                greeting = 'Уважаемая'
            else:
                greeting = 'Уважаемый'
            
            print('{} {}.\n Анализ показал, что с вероятностью %{:.2f} вы мужчина, или %{:.2f} вы женщина. '.format(greeting, name, male, female))


if __name__ == "__main__":
    # execute only if run as a script
    main()
