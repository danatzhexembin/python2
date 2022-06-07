import os

all_lines = []
with open('folder/file.txt', "r", encoding='utf-8') as file:
    for line in file:
        if line != "\n":
            all_lines.append(line[:-1])
print(all_lines)

new_dir_name = 'result'

try:
    # происходит ПОПЫТКА выполнить какой-то код, который может вызвать ошибку

    # путь относительно текущего скрипта
    os.mkdir("folder/" + new_dir_name)
    # connection - объект в памяти, который непрерывно обменивается данными
except:
    # происходит выполнение код, когда код в блоке 'try' вызвал исключение(ошибку)
    print('Папка уже существует!')
finally:
    # происходит выполнение кода, безотносительно удачного или неудачного выполнения
    # тут нужно закрыть соединение с базой данных или файл для чтения/записи
    pass

# print(len(all_lines))
for i in range(len(all_lines)):
    with open(f'folder/result/{all_lines[i]}.txt', "w", encoding='utf-8') as file:
        file.write(all_lines[i])

# удаляет выбранный файл
os.remove("folder/file.txt")
