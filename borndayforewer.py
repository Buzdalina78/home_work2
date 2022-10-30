# модуль 5
# используя условные операторы if-else и цикл while
question = input('Введите год рождения А.С. Пушкина: ')
while question != '1799':
    question = input('НЕ верно. Попробуй еще ')
if question == '1799':
    print('Классно!!! А день и месяц его рождения знаешь ? ')
birthday = input()
while birthday != '6.06' and birthday != '6 июня':
    birthday = input('Неверный день рождения.Подумай еще. ')
if birthday == ('6.06') or birthday == ('6 июня'):
    print('Верно. Молодец ')
print('end')
