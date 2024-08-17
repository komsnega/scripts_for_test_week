# The script to process list (as txt file) of 50 companies published on this page
# https://rentalsunited.com/blog/vacation-rental-property-managers/

# Открываем файл в режиме чтения
with open(r'C:\Users\Pavel\Documents\CV\Sally Test\text_file.txt', 'r', encoding='utf-8') as file:
    # Читаем содержимое файла построчно
    lines = file.readlines()

    # Создаём пустой список для хранения имён
    names = []

    # Перебираем строки файла
    for line in lines:
        # Проверяем, начинается ли строка с числа от 1 до 50
        if line.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50')):
            number, name = line.split('. ', 1)
            names.append(name.strip())

# Выводим список имён
print(names)