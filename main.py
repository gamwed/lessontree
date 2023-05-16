# task 1
# total_floors = 9
# apart_per_floor = 4
# pad = 4
# total_apart = 144
# apart_num = int(input("Кварита ? "))
# if apart_num > total_apart:
#     print("Такой нема!")
# else:
#     print("пад",((apart_num) // (total_floors * apart_per_floor))+1)
#     print("поверх",(((apart_num - 1) % (total_floors * apart_per_floor)) // apart_per_floor)+1)

# task 2
# year = int(input("Введіть рік: "))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     days = 366
# else:
#     days = 365
# print("Кількість днів у році:", days)

# task 3
# a = int(input("A= "))
# b = int(input("B= "))
# c = int(input("C= "))
# print("True - Існуе. False - Не існуе")
# print(a+b > c and a+c > b and b+c > a)

# task 4
# response = input("Володієте посвідченням водія? (yes/no): ")
# answers = ["Ви не можете керувати автомобілем", "Ви можете керувати автомобілем"]
# print(answers[response == "yes"])

# task 5
# age = int(input("Введіть свій вік: "))
# driver_license = input("Чи маєте ви посвідчення водія? (yes/no): ")
# criteria = [age > 18, driver_license.lower() == "yes"]
# messages = ["Ви можете отримати посвідчення водія", "Ви не відповідаєте критеріям для отримання посвідчення водія"]
# print(messages[criteria.count(False)])

