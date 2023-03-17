#python3
tickets_count = int(input("Введите количество билетов: "))
total_cost = 0
discount = 0

# Цикл для подсчета стоимости билетов
for i in range(tickets_count):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        cost = 0
    elif age >= 18 and age <= 25:
        cost = 990
    else:
        cost = 1390
    total_cost += cost

# Проверка на наличие скидки
if tickets_count > 3:
    discount = total_cost * 0.1

# Вывод результата
print("Общая стоимость билетов:", total_cost)
print("Скидка:", discount)
print("Итого к оплате:", total_cost - discount)


